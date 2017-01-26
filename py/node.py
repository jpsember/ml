# Nodes within Func graphs

from tools import *

# Base class
#
class Node:

  def __init__(self):
    self._value = None
    self._gradient = None
    self._links_fwd = []
    self._links_bwd = []
    self._label = None
    self._user = None

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
    """Propagate gradient from node to its parents; base implementation does nothing"""
    pass

  def gradient(self):
    return self._gradient

  def add_to_gradient(self, amount):
    self._gradient += amount

  def set_label(self,label):
    self._label = label

  def label(self):
    return self._label

  def input_node(self, index = 0):
    return self._links_bwd[index]

class ConstNode(Node):

  def __init__(self,value):
    Node.__init__(self)
    self._value = value
    self.set_label(str(value))

  def calculate_value(self):
    return self._value

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

  def propagate_gradient(self):
    for node in self._links_bwd:
      node.add_to_gradient(self.gradient())


class InputNode(Node):

  def __init__(self,matrix_record,row,col):
    Node.__init__(self)
    self._matrix_record = matrix_record
    self._row = row
    self._col = col

  def calculate_value(self):
    return self._matrix_record.matrix().item((self._row,self._col))

  def store_gradient_to_matrix(self):
    self._matrix_record.gradient().itemset((self._row,self._col),self._gradient)


class OutputNode(Node):

  def __init__(self,matrix_record,row,col):
    Node.__init__(self)
    self._matrix_record = matrix_record
    self._row = row
    self._col = col

  def calculate_value(self):
    input = self.input_node().value()
    self._matrix_record.matrix().itemset((self._row,self._col),input)
    return input

  def propagate_gradient(self):
    self._gradient = 1.0
    for node in self._links_bwd:
      node.add_to_gradient(1.0)



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
    self.input_node(0).add_to_gradient(self.gradient() * self.input_node(1).value())
    self.input_node(1).add_to_gradient(self.gradient() * self.input_node(0).value())




class PowNode(Node):

  def __init__(self,power):
    Node.__init__(self)
    self._power = power
    self.set_label("^" + str(self._power))

  def calculate_value(self):
    base = self._links_bwd[0].value()
    return math.pow(self.input_node().value(),self._power)

  def propagate_gradient(self):
    node = self.input_node()
    node.add_to_gradient(self.gradient() * self._power * math.pow(node.value(),self._power - 1))



class InvertNode(Node):

  def __init__(self):
    Node.__init__(self)
    self.set_label("1/x")

  def calculate_value(self):
    input = self.input_node().value()
    return 1.0 / input

  def propagate_gradient(self):
    node = self.input_node()
    node.add_to_gradient(self.gradient() * -1 / (node.value() * node.value()))


