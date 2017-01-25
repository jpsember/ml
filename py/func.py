# Classes for representing a function as a directed graph, with
# ability to evaluate function's value and gradient

from tools import *

# Base class for function graph nodes
#
class Node:

  def __init__(self):
    self._value = None
    self._gradient = None
    self._links_fwd = []
    self._links_bwd = []
    self._label = None
    self._user = None

  def __str__(self):
    s = self.label()
    if self._value is not None:
      s += " value:" + str(self.value())
    if self._gradient is not None:
      s += " grad:" + str(self.gradient())
    return s

  def set_user_value(self, value):
    """Store a value for user usage, e.g., for marking nodes as visited during a sort"""
    self._user = value

  def user_value(self):
    return self._user

  def value(self):
    return self._value

  def calculate_value(self):
    error("unimplemented calculate_value for "+dtype(self))

  def propagate_gradient(self):
    """Propagate gradient from node to its parents"""
    error("unimplemented propagate_gradient for "+dtype(self))

  def gradient(self):
    return self._gradient

  def store_gradient(self, gradient):
    self._gradient = gradient

  def label(self):
    label = self._label
    if label is None:
      label = self.__class__.__name__
    return label

  def set_label(self,label):
    self._label = label

  def input(self, index = 0):
    return self._links_bwd[index]





class ConstNode(Node):

  def __init__(self,value):
    Node.__init__(self)
    self._value = value
    self.set_label(str(value))

  def calculate_value(self):
    return self._value

  def propagate_gradient(self):
    pass

  def __str__(self):
    return str(self.value())

  def gradient(self):
    return 0.0

  def discard_eval(self):
    pass




class AddNode(Node):

  def __init__(self):
    Node.__init__(self)
    self.set_label("+")

  def calculate_value(self):
    sum = 0.
    for node in self._links_bwd:
      sum += node.value()
    return sum

  def propagate_gradient(self):
    for node in self._links_bwd:
      node.store_gradient(self.gradient())


class InputNode(Node):

  def __init__(self,matrix,row,col,matrix_grad):
    Node.__init__(self)
    self._row = row
    self._col = col
    self._matrix = matrix
    self._matrix_grad = matrix_grad

  def calculate_value(self):
    return self._matrix.item((self._row,self._col))

  def propagate_gradient(self):
    pass

  def store_gradient(self, gradient):
    Node.store_gradient(self,gradient)
    self._matrix_grad.itemset((self._row,self._col),gradient)

  def discard_eval(self):
    # Reset value to input matrix
    self._value = self._matrix.item((self._row,self._col))
    self._gradient = None

class OutputNode(Node):

  def __init__(self,matrix,row,col):
    Node.__init__(self)
    self._matrix = matrix
    self._row = row
    self._col = col

  def calculate_value(self):
    input = self.input().value()
    self._matrix.itemset((self._row,self._col),input)
    return input

  def propagate_gradient(self):
    self.store_gradient(1.0)
    for node in self._links_bwd:
      node.store_gradient(1.0)

  def discard_eval(self):
    # Don't discard the gradient (which is constant at 1.0)
    self._value = None


class MultiplyNode(Node):

  def __init__(self):
    Node.__init__(self)
    self.set_label("*")

  def calculate_value(self):
    sum = None
    for node in self._links_bwd:
      value = node.value()
      if sum is None:
        sum = value
      else:
        sum *= value
    return sum

  def propagate_gradient(self):
    self.input(0).store_gradient(self.gradient() * self.input(1).value())
    self.input(1).store_gradient(self.gradient() * self.input(0).value())




class PowNode(Node):

  def __init__(self,power):
    Node.__init__(self)
    self._power = power
    self.set_label("^" + str(self._power))

  def calculate_value(self):
    base = self._links_bwd[0].value()
    return math.pow(self.input().value(),self._power)

  def propagate_gradient(self):
    node = self.input()
    node.store_gradient(self.gradient() * self._power * math.pow(node.value(),self._power - 1))


# Stores information about a named input or output matrix
#
class MatrixRecord:

  def __init__(self, name, matrix):
    self._name = name
    self._matrix = matrix
    self._gradient = None
    self._nodes = None

  @classmethod
  def build_input(cls, name, matrix):
    m = MatrixRecord(name,matrix)
    m.create_gradient()
    m.build_nodes(True)
    return m

  @classmethod
  def build_output(cls, name, matrix):
    m = MatrixRecord(name,matrix)
    m.build_nodes(False)
    return m

  def name(self):
    return self._name

  def matrix(self):
    return self._matrix

  def create_gradient(self):
    """Create a gradient matrix"""
    self._gradient = np.zeros_like(self.matrix())

  def gradient(self):
    return self._gradient

  def build_nodes(self, input_flag):
    self._nodes = []
    previous_row = -1
    node_row = None

    for row,col in np.ndindex(*self.matrix().shape):
      if row != previous_row:
        previous_row = row
        node_row = []
        self._nodes.append(node_row)

      if input_flag:
        node = InputNode(self.matrix(),row,col,self.gradient())
      else:
        node = OutputNode(self.matrix(),row,col)

      node.set_label(self.name() + "[" + str(row) + "," + str(col) + "]")
      node_row.append(node)

  def get_nodes(self):
    return self._nodes

  def get_node(self, row, col):
    return self.get_nodes()[row][col]


class Func:

  def __init__(self):
    self._matrix_records = {}
    self._sorted_nodes = None

  def connect(self, inp_node, out_node):
    self.ensure_prepared(False)
    inp_node._links_fwd.append(out_node)
    out_node._links_bwd.append(inp_node)

  def add_input(self, name, matrix):
    """declare a matrix as an input, and generate corresponding input nodes"""
    self.add_matrix(MatrixRecord.build_input(name,matrix))

  def get_gradient(self, name):
    return self.get_matrix(name).gradient()

  def add_output(self, name, matrix):
    """declare a matrix as an output"""
    self.add_matrix(MatrixRecord.build_output(name,matrix))

  def add_matrix(self, record):
    name = record.name()
    error_if(self._matrix_records.has_key(name),name+" already exists")
    self._matrix_records[name] = record

  def get_matrix(self, name):
    return self._matrix_records[name]

  def inp(self, name, row, col = 0):
    """get node corresponding to element of input matrix"""
    rec = self.get_matrix(name)
    node = rec.get_node(row,col)
    return node

  def out(self, name, row=0, col=0):
    """get node corresponding to element of output matrix"""
    rec = self.get_matrix(name)
    node = rec.get_node(row,col)
    return node

  def add(self, *input_nodes):
    """Construct an AddNode to sum together a list of (two or more) input nodes"""
    error_if(len(input_nodes) == 0)
    adder = AddNode()
    for inp in input_nodes:
      self.connect(inp,adder)
    return adder

  def mult(self, *input_nodes):
    """Construct a MultiplyNode to multiply together a list of two input nodes"""
    error_if(len(input_nodes) != 2)
    multiplier = MultiplyNode()
    for inp in input_nodes:
      self.connect(inp,multiplier)
    return multiplier

  def const(self, value):
    """Construct a ConstNode"""
    return ConstNode(value)

  def square(self, input_node):
    """Construct a PowNode to square inputs"""
    operator = PowNode(2)
    self.connect(input_node,operator)
    return operator

  def ensure_prepared(self, state = True):
    is_prepared = (self._sorted_nodes is not None)
    if state != is_prepared:
      error("unexpected prepared state")

  # Prepare graph for processing; no further structural changes can occur
  def prepare(self):
    self.ensure_prepared(False)
    self._sorted_nodes = self.get_sorted_nodes()

  def sorted_nodes(self):
    return self._sorted_nodes

  def evaluate(self):
    """Evaluate outputs of function (and all intermediate nodes),
    including the gradient"""

    self.ensure_prepared()

    for node in self.sorted_nodes():
      node.store_gradient(0)
      node._value = node.calculate_value()
    for node in reversed(self.sorted_nodes()):
      node.propagate_gradient()

  def get_all_nodes(self):
    """Build a list of all nodes in graph"""
    # We will assume that every node in the graph is connected to an input or output;
    # and we ought to be able to assume that every node (including, e.g., constants)
    # has a forward path to an output node
    nodes = set()

    stack = []
    for rec in self._matrix_records.values():
      for row in rec.get_nodes():
        stack += row
    while len(stack) != 0:
      node = stack.pop()
      if not node in nodes:
        nodes.add(node)
        stack += node._links_bwd
        stack += node._links_fwd
    return list(nodes)

  def get_sorted_nodes(self):
    """Build a topologically-sorted list of nodes"""

    all_nodes_list = self.get_all_nodes()
    for node in all_nodes_list:
      node.set_user_value(None)

    top_sort = []
    for node in all_nodes_list:
      self.visit_node(node, top_sort)

    sort_val = 0
    for node in top_sort:
      node.set_user_value(sort_val)
      sort_val += 1
    return top_sort

  def visit_node(self, node, top_sort):
    if node.user_value() is not None:
      return
    for parent in node._links_bwd:
      self.visit_node(parent, top_sort)
    node.set_user_value(True)
    top_sort.append(node)

  def name_of_node(self, node):
    return str(self.sorted_nodes().index(node))

  def make_dotfile(self, filename = "func"):

    s ="digraph func {\n"
    s += "rankdir=\"LR\";\n\n"

    for node in self.sorted_nodes():
      name = self.name_of_node(node)
      s += "  " + name + "["
      shape = "box"
      s += 'shape="' + shape + '" '

      if node.__class__ == InputNode or node.__class__ == OutputNode:
        s += 'style=bold '
      s += 'label="'
      s += node.label()

      # Include topological sort values
      q = node.user_value()
      if q is not None:
        s += "(sort:" + str(q)+")"
        s += '\\n'

      if node.__class__ != ConstNode:
        s += '\\n\\n'
        if node._value is not None:
          s += str(node._value)
        s += '\\n'
        if node._gradient is not None:
          s += str(node.gradient())
      s += '"];'
      s += "\n"
      for child in node._links_fwd:
        s += "  " + name + " -> " + self.name_of_node(child) + ";\n"
      s += "\n"
    s += "}\n"

    text_file = open(filename + ".dot","w")
    text_file.write(s)
    text_file.close()
    return s
