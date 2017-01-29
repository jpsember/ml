#! /usr/bin/env python

# Experiments with back propagation
# See: http://cs231n.github.io/optimization-2/

import numpy as np
import math
from func import *

NUM_CLASSES = 3
DATA_DIM = 3  # includes bias value, always 1.0

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

def calculated_type(score_nodes):
  max_val = None
  best_type = None
  type = 0
  # Todo: clarify why we're looking at row instead of column here
  for score_node in score_nodes[0]:
    val = score_node.value()
    if max_val is None or max_val < val:
      max_val = val
      best_type = type
    type += 1
  return best_type


np.random.seed(1965)

train_samples,train_types = build_spiral_data(100,NUM_CLASSES)


# Define matrices containing the layers, data inputs, and cost



data = mat(DATA_DIM,np.zeros(DATA_DIM))
data[0,DATA_DIM-1] = 1

data_type = mat(1,np.zeros(1))

cost = mat(1,[0])

NET_SIZE = 100 # size of hidden layer

SMALL = (NET_SIZE <= 20)

w1 = np.random.randn(DATA_DIM, NET_SIZE)
w2 = np.random.randn(NET_SIZE, NUM_CLASSES)



f = Func()

f.add_data("d", data)
f.add_data("y",data_type)
f.add_input("w1", w1)
f.add_input("w2", w2)

f.add_output("f",cost)

# Generate matrix record for multiplication
f.mult_matrix("d","w1","l1");

# Generate nodes representing ReLU activation of a set of nodes
f.relu_matrix("l1","relu")

score_rec = f.mult_matrix("relu","w2","s")

score_nodes = score_rec.get_nodes()

svm_node = f.svm_loss(f.elem("y",0), score_nodes)
reg_node = f.reg_loss("relu",0.1)
f.connect(f.add(svm_node, reg_node),f.elem("f"))

f.prepare()


# Perform gradient descent iterations

done = False
previous_cost = None

max_reps = 75
epsilon = 1e-7
speed = 0.3
accel = 1.3

reps = 0
while not done:
  if reps < 20:
    speed = 0.7
  elif reps < 30:
    speed = 0.25
  else:
    speed = 0.1

  # Iterate over all the training samples, plugging each into the function
  # and summing the cost and gradients produced
  num_samples = len(train_samples)
  gradient_sum_w1 = np.zeros_like(f.get_gradient("w1"))
  gradient_sum_w2 = np.zeros_like(f.get_gradient("w2"))
  cost_sum = 0

  for train_index in range(num_samples):
    train_sample = train_samples[train_index]
    data[0,0] = train_sample[0]
    data[0,1] = train_sample[1]

    data_type[0] = train_types[train_index]

    f.evaluate()
    gradient_sum_w1 += f.get_gradient("w1")
    gradient_sum_w2 += f.get_gradient("w2")

    current_cost = cost.item((0,0))
    cost_sum += current_cost

  # Replace cost/gradient sums with averages
  current_cost = cost_sum / num_samples
  gradient_sum_w1 *= (1.0 / num_samples)
  gradient_sum_w2 *= (1.0 / num_samples)

  reps += 1

  pr("Rep: %2d Cost:%s Speed:%s\n",
     reps,
     df(current_cost),
     df(speed))

  if reps == max_reps:
    done = True

  if previous_cost is not None:
    delta = abs(current_cost - previous_cost)
    if delta < epsilon:
      done = True
      break

  previous_cost = current_cost

  parameters = f.get_matrix("w1").matrix()
  parameters += (-speed) * gradient_sum_w1

  if SMALL:
    print "Trained parameters w1:"
    print dm(parameters)

  parameters = f.get_matrix("w2").matrix()
  parameters += (-speed) * gradient_sum_w2
  if SMALL:
    print "Trained parameters w2:"
    print dm(parameters)

  if SMALL and reps == 12:
    f.make_dotfile("spiral")

# Determine accuracy of function relative to training set

correct_count = 0
n_samples = len(train_samples)
for i in range(n_samples):
  x,y = train_samples[i]
  data[0,0] = x
  data[0,1] = y
  f.evaluate()
  eval_type = calculated_type(score_nodes)
  if train_types[i] == eval_type:
    correct_count += 1

print "Accuracy:",df(correct_count / float(n_samples))


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
    data[0,1] = y

    f.evaluate()
    ls = results[calculated_type(score_nodes)]
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

