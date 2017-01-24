#! /usr/bin/env python

# Experiments with back propagation
# See: http://cs231n.github.io/optimization-2/

import numpy as np
import math
from func import *


f = Func()
f.add_input("w", mat(1,[0,0]))
f.add_output("f", mat(1,[0]))

x = f.input_node("w",0)
y = f.input_node("w",1)

n = f.add(f.square(f.add(x,f.const(-5))),f.square(f.add(y,f.const(-3))))

output = f.output_node("f")

f.connect(n,output)

f.evaluate()

f.make_dotfile("quadratic")
