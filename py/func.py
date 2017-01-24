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

  def link_to(self,other):
    self._links_fwd.append(other)
    other._links_bwd.append(self)

  def value(self):
    if self._value is None:
      self._value = self.calculate_value()
    return self._value

  def calculate_value(self):
    error("unimplemented calculate_value for "+dtype(self))

  def gradient(self):
    if self._gradient is None:
      self._gradient = self.calculate_gradient()
    return self._gradient

  def calculate_gradient(self):
    error("unimplemented calculate_gradient for "+dtype(self))

  def label(self):
    label = self._label
    if label is None:
      label = self.__class__.__name__
    return label

  def is_io(self):
    return False

  def set_label(self,label):
    self._label = label




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


class AddNode(Node):

  def __init__(self):
    Node.__init__(self)
    self.set_label("+")

  def calculate_value(self):
    sum = 0.
    for node in self._links_bwd:
      sum += node.value()
    return sum


class InputNode(Node):

  def __init__(self,matrix,row,col):
    Node.__init__(self)
    self._value = matrix.item((row,col))

  def is_io(self):
    return True


class OutputNode(Node):

  def __init__(self,matrix,row,col):
    Node.__init__(self)
    self._matrix = matrix
    self._row = row
    self._col = col

  def calculate_value(self):
    input = self._links_bwd[0].value()
    self._matrix.itemset((self._row,self._col),input)
    return input

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


class PowNode(Node):

  def __init__(self,power):
    Node.__init__(self)
    self.__power = power
    self.set_label("^" + str(self.__power))

  def calculate_value(self):
    base = self._links_bwd[0].value()
    return math.pow(base,self.__power)



class Func:

  def __init__(self):
    self._matrices = {}
    self._nodes = {}
    self._node_set = None

  def add_input(self, name, matrix):
    error_if(self._matrices.has_key(name),name+" already exists")
    self._matrices[name] = matrix

  def add_output(self, name, matrix):
    error_if(self._matrices.has_key(name),name+" already exists")
    self._matrices[name] = matrix

  def input_node(self, name, row, col):
    expr = name+"_"+str(row)+","+str(col)
    node = self._nodes.get(expr)
    if node is None:
      matrix = self._matrices[name]
      node = InputNode(matrix,row,col)
      self._nodes[expr] = node
      node.set_label(name + "[" + str(row) + "," + str(col) + "]")
    return node

  def output_node(self, name, row, col):
    expr = name+"_"+str(row)+","+str(col)
    node = self._nodes.get(expr)
    if node is None:
      matrix = self._matrices[name]
      node = OutputNode(matrix,row,col)
      self._nodes[expr] = node
      node.set_label(name + "[" + str(row) + "," + str(col) + "]")
    return node

  def evaluate(self):
    for node in self.node_set():
      node.value()

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

  def make_dotfile(self):

    s ="digraph func {\n"
    s += "rankdir=\"LR\";\n"

    # Generate dot file

    for node in self.node_set():
      name = self._node_names[node]
      s += name + "["
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
        s += name + " -> " + self._node_names[child] + ";\n"
    s += "}\n"

    text_file = open("func.dot","w")
    text_file.write(s)
    text_file.close()
    return s
