# Classes for representing a function as a directed graph, with
# ability to evaluate function's value and gradient

from tools import *

from node import *

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
        node = InputNode(self,row,col)
      else:
        node = OutputNode(self,row,col)

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

  def invert(self, input_node):
    operator = InvertNode()
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
      node._gradient = 0.0
      node._value = node.calculate_value()
    for node in reversed(self.sorted_nodes()):
      node.propagate_gradient()

    self.read_gradients_from_input_nodes()

  def read_gradients_from_input_nodes(self):
    for node in self.sorted_nodes():
      if node.__class__ != InputNode:
        continue
      node.store_gradient_to_matrix()

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

  def fmt_float(self, value):
    return "{:7.3f}".format(value)

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

      if node.__class__ != ConstNode:
        s += '\\n\\n'
        if node._value is not None:
          s += self.fmt_float(node._value)
        s += '\\n'
        if node._gradient is not None:
          s += self.fmt_float(node.gradient())
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
