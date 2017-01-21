#! /usr/bin/env python

# Experiments with back propagation
# See: http://cs231n.github.io/optimization-2/

import numpy as np
import math

def evaluate(input):

  # Perform back propagation to minimize (x-5)^2 + (y-3)^2

  x,y = input

  a1 = x - 5
  a2 = math.pow(a1,2)
  a3 = y - 3
  a4 = math.pow(a3,2)
  a5 = a2 + a4

  result = a5

  # Perform backpropagation

  bx = 0
  by = 0

  b5 = 1

  b2 = b5
  b4 = b5

  b1 = b2 * (2 * a1)

  b3 = b4 * (2 * a3)

  bx += b1

  by += b3

  gradient = np.array([bx,by])

  return gradient,result


def optimize(input):

  speed = 0.1

  location = input.astype(float)

  iter = 0
  while True:
    gradient, value = evaluate(location)
    print "loc :",location,"grad:",gradient,"val :",value

    # If value hasn't changed much, stop iterations
    if iter != 0 and abs(value - value_prev) < 1e-5:
      break

    value_prev = value

    # We're minimizing, so move opposite to gradient direction
    location +=  gradient * -speed

    iter += 1
    if iter == 30:
      break


optimize(np.array([1,1]))
