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

  def __str__(self):
    s = self.label()
    if self._value is not None:
      s += " value:" + str(self.value())
    if self._gradient is not None:
      s += " grad:" + str(self.gradient())
    return s

  def value(self):
    if self._value is None:
      self._value = self.calculate_value()
    return self._value

  def calculate_value(self):
    error("unimplemented calculate_value for "+dtype(self))

  def gradient(self):
    if self._gradient is None:
      # Ask child node to calculate its gradient
      self.output().calculate_gradients()
    return self._gradient

  def calculate_gradients(self):
    """Calculate this node's gradient, plus those of its parent nodes"""
    error("unimplemented calculate_gradients for "+dtype(self))

  def store_gradient(self, gradient):
    self._gradient = gradient

  def discard_eval(self):
    self._gradient = None
    self._value = None

  def label(self):
    label = self._label
    if label is None:
      label = self.__class__.__name__
    return label

  def is_io(self):
    return False

  def set_label(self,label):
    self._label = label

  def inputs(self):
    return len(self._links_bwd)

  def input(self, index = 0):
    return self._links_bwd[index]

  def outputs(self):
    return len(self._links_fwd)

  def output(self, index = 0):
    return self._links_fwd[index]




class ConstNode(Node):

  def __init__(self,value):
    Node.__init__(self)
    self._value = value
    self.set_label(str(value))

  def calculate_value(self):
    sum = 0.
    for node in self._links_bwd:
      sum += node.value()
    return sum

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

  def calculate_gradients(self):
    for node in self._links_bwd:
      node.store_gradient(self.gradient())


class InputNode(Node):

  def __init__(self,matrix,row,col,matrix_grad):
    Node.__init__(self)
    self._row = row
    self._col = col
    self._matrix = matrix
    self._matrix_grad = matrix_grad
    self._value = matrix.item((row,col))

  def is_io(self):
    return True

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
    self.store_gradient(1.0)

  def calculate_value(self):
    input = self.input().value()
    self._matrix.itemset((self._row,self._col),input)
    return input

  def calculate_gradients(self):
    for node in self._links_bwd:
      node.store_gradient(1.0)

  def is_io(self):
    return True

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

  def calculate_gradients(self):
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

  def calculate_gradients(self):
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
    self._node_set = None

  def connect(self, inp_node, out_node):
    inp_node._links_fwd.append(out_node)
    out_node._links_bwd.append(inp_node)

  def add_input(self, name, matrix):
    """declare a matrix as an input, and generate corresponding input nodes"""
    m = self.add_matrix(name,matrix)
    m.create_gradient()
    m.build_nodes(True)

  def get_gradient(self, name):
    m = self.get_matrix(name)
    return m.gradient()

  def add_output(self, name, matrix):
    """declare a matrix as an output"""
    m = self.add_matrix(name,matrix)
    m.build_nodes(False)

  def add_matrix(self, name, matrix):
    error_if(self._matrix_records.has_key(name),name+" already exists")
    record = MatrixRecord(name,matrix)
    self._matrix_records[name] = record
    return record

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

  def evaluate(self):
    """Evaluate outputs of function (and all intermediate nodes),
    including the gradient"""
    for node in self.node_set():
      node.discard_eval()
    for node in self.node_set():
      node.value()
      node.gradient()

  def node_set(self):
    """Build set of nodes as closure of graph"""
    if self._node_set is None:
      nodes = set()
      self._node_names = {}

      stack = []

      # Add all nodes from matrix record to stack
      for rec in self._matrix_records.values():
        for row_list in rec.get_nodes():
          stack += row_list

      while len(stack) != 0:
        node = stack.pop()
        if not node in nodes:
          nodes.add(node)
          self._node_names[node] = str(len(self._node_names))
          stack += node._links_bwd
          stack += node._links_fwd
      self._node_set = nodes
    return self._node_set

  def make_dotfile(self, filename = "func"):

    s ="digraph func {\n"
    s += "rankdir=\"LR\";\n\n"

    # Generate dot file

    for node in self.node_set():
      name = self._node_names[node]
      s += "  " + name + "["
      shape = "box"
      s += 'shape="' + shape + '" '
      if node.is_io():
        s += 'style=bold '
      s += 'label="'
      s += node.label()
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
        s += "  " + name + " -> " + self._node_names[child] + ";\n"
      s += "\n"
    s += "}\n"

    text_file = open(filename + ".dot","w")
    text_file.write(s)
    text_file.close()
    return s

