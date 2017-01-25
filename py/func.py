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
    self._matrix_grad = matrix_grad
    self._value = matrix.item((row,col))

  def is_io(self):
    return True

  def store_gradient(self, gradient):
    Node.store_gradient(self,gradient)
    self._matrix_grad.itemset((self._row,self._col),gradient)


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


class Func:

  def __init__(self):
    self._matrices = {}
    self._nodes = {}
    self._node_set = None

  def connect(self, inp_node, out_node):
    inp_node._links_fwd.append(out_node)
    out_node._links_bwd.append(inp_node)

  def add_input(self, name, matrix):
    """declare a matrix as an input, and generate corresponding input nodes"""
    error_if(self._matrices.has_key(name),name+" already exists")
    self._matrices[name] = matrix
    grad_name = self._gradient_matrix_name(name)
    self._matrices[grad_name] = np.zeros_like(matrix)
    # Define nodes for individual elements
    for row,col in np.ndindex(*matrix.shape):
      self.inp(name,row,col)

  def get_gradient(self, name):
    return self._matrices[self._gradient_matrix_name(name)]

  def add_output(self, name, matrix):
    """declare a matrix as an output"""
    error_if(self._matrices.has_key(name),name+" already exists")
    self._matrices[name] = matrix
    # Define nodes for individual elements
    for row,col in np.ndindex(*matrix.shape):
      self.out(name,row,col)

  def inp(self, name, row, col = 0):
    """get node (generating if necessary) corresponding to element of input matrix"""
    expr = name+"_"+str(row)+","+str(col)
    node = self._nodes.get(expr)
    if node is None:
      matrix = self._matrices[name]
      grad_matrix = self._matrices[self._gradient_matrix_name(name)]
      node = InputNode(matrix,row,col,grad_matrix)
      self._nodes[expr] = node
      node.set_label(name + "[" + str(row) + "," + str(col) + "]")
    return node

  def out(self, name, row=0, col=0):
    """get node (generating if necessary) corresponding to element of output matrix"""
    expr = name+"_"+str(row)+","+str(col)
    node = self._nodes.get(expr)
    if node is None:
      matrix = self._matrices[name]
      node = OutputNode(matrix,row,col)
      self._nodes[expr] = node
      node.set_label(name + "[" + str(row) + "," + str(col) + "]")
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
    if not already done; also evaluate the gradient"""
    for node in self.node_set():
      node.value()
      node.gradient()

  def node_set(self):
    """Build set of nodes as closure of graph"""
    if self._node_set is None:
      nodes = set()
      self._node_names = {}
      stack = self._nodes.values()
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

  @staticmethod
  def _gradient_matrix_name(matrix_name):
    return matrix_name + "_g"
