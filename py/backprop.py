#! /usr/bin/env python

# Experiments with back propagation
# See: http://cs231n.github.io/optimization-2/

import numpy as np
import math
from func import *

# Let's try minimizing this function:
#
#   - max(2x,3y)    <--- the negative sign is so we can always be minimizing
# --------------
# (1 + x^2 + y^2)
#


# Construct matrices for cost function; parameters (input), cost (output)
#
parameters = mat(1,[0,0])
cost = mat(1,[0])

# Also include a data matrix, which we can use to plug in different training samples, for instance
data = mat(1,[2,3])

# Construct a graph representing the cost function
#

f = Func()

f.add_input("w", parameters)
f.add_output("f", cost)
f.add_data("d", data)

x = f.elem("w",0)
y = f.elem("w",1)

numer = f.max(f.mult(f.elem("d",0),x), f.mult(f.elem("d",1),y))
numer = f.mult(f.const(-1),numer)
denom = f.add(f.const(1), f.square(x), f.square(y))

loss_node = f.div(numer,denom)
reg_node = f.reg_loss("w",0.1)
sum_node = f.add(loss_node,reg_node)

f.connect(sum_node,f.elem("f"))
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
  if reps == 4:
    f.make_dotfile("max")

  current_cost = cost.item((0,0))
  reps += 1

  np.set_printoptions(precision=3, suppress = True)
  pr("Rep: %2d Param:%s Cost:%s Grad:%s Speed:%s\n",
     reps,
     dm(col(parameters,0)),
     df(current_cost),
     dm(col(gradient,0)),
     df(speed))

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

  add = (-speed) * gradient

  previous_param = parameters.copy()
  previous_gradient = gradient.copy()

  parameters += add


