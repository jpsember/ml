#! /usr/bin/env python

# Experiments with back propagation
# See: http://cs231n.github.io/optimization-2/

import numpy as np
import math
from func import *


# Let's build a function to evaluate (x+y)z  (from the lecture notes)
# at [-2,5,-4]

f = Func()
f.add_input("w", mat(1,[-2,5,-4]))
f.add_output("f", mat(1,[0]))

x = f.input_node("w",0,0)
y = f.input_node("w",1,0)
z = f.input_node("w",2,0)

n1 = f.mult(f.add(x,y),z)

output = f.output_node("f",0,0)
n1.link_to(output)

f.evaluate()

f.make_dotfile("x_plus_y_times_z")
