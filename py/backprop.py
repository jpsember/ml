#! /usr/bin/env python

# Experiments with back propagation
# See: http://cs231n.github.io/optimization-2/

import numpy as np
import math
from func import *

# Construct matrices for cost function; parameters (input), cost (output)
#
parameters = mat(1,[0,0])
cost = mat(1,[0])

# Construct a graph representing the cost function
#
f = Func()

f.add_input("w", parameters)
f.add_output("f", cost)

x = f.inp("w",0)
y = f.inp("w",1)

n = f.add(f.square(f.add(x,f.const(-5))),f.square(f.add(y,f.const(-3))))

f.connect(n,f.out("f"))
f.prepare()

# Perform gradient descent iterations

done = False
previous_cost = None

reps = 0
while not done:
  f.evaluate()
  gradient = f.get_gradient("w")
  if reps == 0:
    f.make_dotfile("quadratic")

  current_cost = cost.item((0,0))
  reps += 1

  np.set_printoptions(precision=3, suppress = True)
  pr("Rep: %2d Param:%s Cost:%8.6f Grad:%s\n",
     reps,
     col(parameters,0).transpose(),
     current_cost,
     col(gradient,0).transpose())

  if reps > 50:
    done = True

  if previous_cost is not None:
    delta = abs(current_cost - previous_cost)
    if delta < 1e-5:
      done = True
  previous_cost = current_cost

  add = -0.1 * gradient
  parameters += add


