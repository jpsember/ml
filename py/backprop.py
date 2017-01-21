#! /usr/bin/env python

# Experiments with back propagation
# See: http://cs231n.github.io/optimization-2/

import numpy as np

def evaluate(input):

  # Perform back propagation to optimize max(3(x+2y),z)

  x,y,z = input

  i1 = 2 * y
  i2 = i1 + x
  i3 = 3 * i2
  i4 = max(z,i3)
  result = i4

  # Perform backpropagation

  # Define gradient variables j* corresponding to input nodes x,y,z and intermediate
  # nodes i*.

  # 'Gradients add up at forks.'
  #
  # Initialize the gradients at the input variables (x,y,z) to zero, and
  # when storing to them, add to the accumulators jx,jy,jz.
  #

  jx = 0
  jy = 0
  jz = 0

  # Backprop the result i4; it's always 1 (why?)
  #
  j4 = 1

  # Backprop i4 (max)
  #
  jz += j4 * (j4 if z > i3 else 0)
  j3 = j4 * (j4 if i3 > z else 0)


  # Backprop i3 (3 * i2)
  #
  j2 = j3 * 3

  # Backprop i2 (i1 + x)
  #
  j1 = j2
  jx += j2

  # Backprop i1 (2 * y)
  #
  jy += 2 * j1

  gradient = np.array([jx,jy,jz])

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
    location +=  gradient * speed

    iter += 1
    if iter == 20:
      break


optimize(np.array([5,2,12]))
