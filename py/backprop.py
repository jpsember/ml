#! /usr/bin/env python

# Experiments with back propagation
# See: http://cs231n.github.io/optimization-2/

import numpy as np
import math
from func import *

f = Func()

f.add_input("w", mat(1,[0,0]))
f.add_output("f", mat(1,[0]))

x = f.inp("w",0)
y = f.inp("w",1)

n = f.add(f.square(f.add(x,f.const(-5))),f.square(f.add(y,f.const(-3))))

f.connect(n,f.out("f"))

f.evaluate()

f.make_dotfile("quadratic")
