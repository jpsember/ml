#! /usr/bin/env python

# Experiments with back propagation
# See: http://cs231n.github.io/optimization-2/

import numpy as np
import math
from func import *

# Let's try maximizing this function:
#
#    x + y
# ----------------------
# 1 + (x+2)^2 + (y-3)^2
#


def fmt_float(value):
  return "{:7.3f}".format(value)


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

n1 = f.add(x,y)
n2 = f.square(f.add(x,f.const(2)))
n3 = f.square(f.add(y,f.const(-3)))
n4 = f.add(f.const(1),n2,n3)
n5 = f.invert(n4)
n6 = f.mult(n1,n5)

f.connect(n6,f.out("f"))
f.prepare()

# Perform gradient descent iterations

done = False
previous_cost = None
previous_param = None
previous_gradient = None

max_reps = 60
epsilon = 1e-7
speed = 0.3
accel = 1.3

reps = 0
while not done:
  f.evaluate()
  gradient = f.get_gradient("w")
  if reps == max_reps/3:
    f.make_dotfile("quadratic")

  current_cost = cost.item((0,0))
  reps += 1

  np.set_printoptions(precision=3, suppress = True)
  pr("Rep: %2d Param:%s Cost:%s Grad:%s Speed:%s\n",
     reps,
     col(parameters,0).transpose(),
     fmt_float(current_cost),
     col(gradient,0).transpose(),
     fmt_float(speed))

  if reps == max_reps:
    done = True

  if previous_cost is not None:
    delta = abs(current_cost - previous_cost)
    if delta < epsilon:
      done = True
      break

    if previous_cost > current_cost:
      speed = speed * accel
    else:
      # Restore original parameters
      np.copyto(parameters, previous_param)
      np.copyto(gradient, previous_gradient)
      # Reduce speed
      speed = speed * 0.2

  previous_cost = current_cost

  add = -speed * gradient
  previous_param = parameters.copy()
  previous_gradient = gradient.copy()

  parameters += add


