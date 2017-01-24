#! /usr/bin/env python

# Experiments with back propagation
# See: http://cs231n.github.io/optimization-2/

import numpy as np
import math
from func import *


# Let's build a function to minimize (x-5)^2 + (y-3)^2
#
# We'll set m = [x
#                y]

f = Func()
f.add_input("w", mat(1,[.1,.1]))
f.add_output("f", mat(1,[0]))

x = f.input_node("w",0,0)
y = f.input_node("w",1,0)

n0 = ConstNode(-5)

n1 = AddNode()

n0.link_to(n1)
x.link_to(n1)

n2 = PowNode(2)
n1.link_to(n2)

m0 = ConstNode(-3)

m1 = AddNode()

m0.link_to(m1)
y.link_to(m1)

m2 = PowNode(2)
m1.link_to(m2)

n4 = AddNode()
n2.link_to(n4)
m2.link_to(n4)

output = f.output_node("f",0,0)
n4.link_to(output)

print "output:",output.value()

f.make_dotfile()

