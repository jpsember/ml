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




np.random.seed(1965)

train_samples,train_types = build_spiral_data(10,NUM_CLASSES)





DATA_DIM = 3  # includes bias value, always 1.0

parameters = 0.01 * np.random.randn(DATA_DIM, NUM_CLASSES)

# Also include a data matrix, with which we will plug in the different training samples
data = mat(1,np.zeros(DATA_DIM))
data[2,0] = 1 # this is always 1

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

max_reps = 50
epsilon = 1e-7
speed = 0.3
accel = 1.3

reps = 0
while not done:

  # Iterate over all the training samples, plugging each into the function
  # and summing the cost and gradients produced
  num_samples = len(train_samples)
  gradient_sum = np.zeros_like(f.get_gradient("w"))
  cost_sum = 0

  for train_index in range(num_samples):
    train_sample = train_samples[train_index]
    data[0,0] = train_sample[0]
    data[1,0] = train_sample[1]

    data_type[0] = train_types[train_index]

    f.evaluate()
    gradient = f.get_gradient("w")
    gradient_sum += gradient

    current_cost = cost.item((0,0))
    cost_sum += current_cost

  # Replace cost/gradient sums with averages
  current_cost = cost_sum / num_samples
  gradient_sum *= (1.0 / num_samples)
  gradient = gradient_sum

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

  if reps == 12:
    f.make_dotfile("max")

