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

  def __str__(self):
    s = self.__class__.__name__
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



class ConstNode(Node):

  def __init__(self,value):
    Node.__init__(self)
    self._value = value

  def calculate_value(self):
    sum = 0.
    for node in self._links_bwd:
      sum += node.value()
    return sum

  def __str__(self):
    return str(self.value())



class AddNode(Node):

  def calculate_value(self):
    sum = 0.
    for node in self._links_bwd:
      sum += node.value()
    return sum



class MultiplyNode(Node):

  def calculate_value(self):
    sum = None
    for node in self._links_bwd:
      value = node.value()
      if sum is None:
        sum = value
      else:
        sum *= value
    return sum


