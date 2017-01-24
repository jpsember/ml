#! /usr/bin/env python

# Experiments with back propagation
# See: http://cs231n.github.io/optimization-2/

import numpy as np
import math
from func import *


x = ConstNode(12)
z = ConstNode(7)

y = AddNode()
x.link_to(y)
z.link_to(y)

m = MultiplyNode()
n = ConstNode(6)
y.link_to(m)
n.link_to(m)


print "Nodes, before evaluation:"
print x
print y
print z
print m
print n

m.value()

print "Nodes, after evaluation:"
print x
print y
print z
print m
print n



