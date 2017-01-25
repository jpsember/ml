#! /usr/bin/env python

# Experiments with back propagation
# See: http://cs231n.github.io/optimization-2/

import numpy as np
import math
from func import *

objective = mat(1,[0,0])
output = mat(1,[0])
done = False
previous_value = None

reps = 0
while not done:

  f = Func()

  f.add_input("w", objective)
  f.add_output("f", output)

  x = f.inp("w",0)
  y = f.inp("w",1)

  n = f.add(f.square(f.add(x,f.const(-5))),f.square(f.add(y,f.const(-3))))

  f.connect(n,f.out("f"))

  f.evaluate()

  f.make_dotfile("quadratic")

  current_value = output.item((0,0))
  reps += 1

  np.set_printoptions(precision=3,suppress = True)
  pr("Rep: %2d Val:%8.6f Obj:%s\n",reps,current_value,col(objective,0).transpose())

  if reps > 50:
    done = True

  if previous_value is not None:
    delta = abs(current_value - previous_value)
    if delta < 1e-5:
      done = True
  previous_value = current_value

  g = f.get_gradient("w")
  add = -0.1 * g
  objective += add



