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
score_nodes = []
for k in range(NUM_CLASSES):
  mult_nodes = []
  for i in range(3):
    w = f.elem("w",k,i)
    x = f.elem("d",i)
    m = f.mult(w,x)
    mult_nodes.append(m)
  sum_node = f.add(*mult_nodes)
  score_nodes.append(sum_node)

svm_node = f.svm_loss(f.elem("y",0), score_nodes)


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
    f.make_dotfile("spiral")

print "Trained parameters:"
print dm(parameters)


# Now evaluate function for a grid of points
#

results = []
for i in range(NUM_CLASSES):
  results.append([[],[]])

RES = 50
for yi in range(RES):
  y = 2 * (yi - RES/2) / float(RES)
  for xi in range(RES):
    x = 2 * (xi - RES/2) / float(RES)

    data[0,0] = x
    data[1,0] = y

    f.evaluate()

    max_val = None
    best_type = None
    type = 0
    for score_node in score_nodes:
      val = score_node.value()
      if max_val is None or max_val < val:
        max_val = val
        best_type = type
      type += 1

    ls = results[best_type]
    ls[0].append(x)
    ls[1].append(y)


type = 0
colors = ['m.','y.','c.']
for ls in results:
  plt.plot(ls[0],ls[1],colors[type])
  type += 1

colors2 = ['ro','go','bo']
for train_index in range(len(train_samples)):
  train_sample = train_samples[train_index]
  x = train_sample[0]
  y = train_sample[1]
  plt.plot(x,y,colors2[train_types[train_index]])

save_plot()

