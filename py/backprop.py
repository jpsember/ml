#! /usr/bin/env python

# Experiments with back propagation
# See: http://cs231n.github.io/optimization-2/

import numpy as np
import math
from func import *

NUM_CLASSES = 3

def build_spiral_data(points_per_class = 100, num_classes = NUM_CLASSES):
  X = np.zeros((points_per_class*num_classes,2)) # data matrix (each row = single example)
  y = np.zeros(points_per_class*num_classes, dtype='uint8') # class labels
  for j in xrange(num_classes):
    ix = range(points_per_class*j,points_per_class*(j+1))
    r = np.linspace(0.0,1,points_per_class) # radius
    t = np.linspace(j*4,(j+1)*4,points_per_class) + np.random.randn(points_per_class)*0.2 # theta
    X[ix] = np.c_[r*np.sin(t), r*np.cos(t)]
    y[ix] = j
  return (X,y)


DATA_DIM = 3  # includes bias value, always 1.0

parameters = 0.01 * np.random.randn(DATA_DIM, NUM_CLASSES)

# Also include a data matrix, with which we will plug in the different training samples
data = mat(1,np.zeros(DATA_DIM))
data_type = mat(1,np.zeros(1))



f = Func()

f.add_input("w", parameters)
f.add_data("d", data)
f.add_data("y",data_type)

# Construct nodes S representing matrix multiplication W x D
#
s = []
for k in range(NUM_CLASSES):
  mult_nodes = []
  for i in range(3):
    w = f.elem("w",k,i)
    x = f.elem("d",i)
    m = f.mult(w,x)
    mult_nodes.append(m)
  sum_node = f.add(*mult_nodes)
  s.append(sum_node)

svm_node = f.svm_loss(f.elem("y",0), s)


cost = mat(1,[0])
f.add_output("f",cost)

reg_node = f.reg_loss("w",0.1)
f.connect(f.add(svm_node, reg_node),f.elem("f"))

f.prepare()


# Perform gradient descent iterations

done = False
previous_cost = None
previous_param = None
previous_gradient = None

max_reps = 8 # temporary: until SVM loss implemented
epsilon = 1e-7
speed = 0.3
accel = 1.3

reps = 0
while not done:

  # Plug in sample data
  # (todo: iterate over all sample data values, accumulating gradient for each)
  data[0,0] = 5
  data[1,0] = 7
  data[2,0] = -3
  data_type[0] = NUM_CLASSES / 2

  f.evaluate()
  gradient = f.get_gradient("w")
  if reps == 0:
    f.make_dotfile("max")

  current_cost = cost.item((0,0))
  reps += 1

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
