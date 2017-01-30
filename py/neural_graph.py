#! /usr/bin/env python

# Represent a neural network as a graph,
# train it to assign colors to the 'spiral' points
#

import numpy as np
import math
from func import *

NUM_CLASSES = 3
NET_SIZE = 100 # size of hidden layer

class App:


  def run(self):
    np.random.seed(1965)
    self.build_spiral_data(100,NUM_CLASSES)
    self.define_matrices()
    self.define_function()
    self.perform_gradient_descent()
    self.evaluate_accuracy()
    self.apply_function_to_grid()
    self.plot_grid_results()
    self.plot_train_samples()
    save_plot()


  def build_spiral_data(self, points_per_class = 100, num_classes = NUM_CLASSES):
    X = np.zeros((points_per_class*num_classes,2)) # data matrix (each row = single example)
    y = np.zeros(points_per_class*num_classes, dtype='uint8') # class labels
    for j in xrange(num_classes):
      ix = range(points_per_class*j,points_per_class*(j+1))
      r = np.linspace(0.0,1,points_per_class) # radius
      t = np.linspace(j*4,(j+1)*4,points_per_class) + np.random.randn(points_per_class)*0.2 # theta
      X[ix] = np.c_[r*np.sin(t), r*np.cos(t)]
      y[ix] = j
    self.train_samples = X
    self.train_types = y


  def calculated_type(self):
    """Determine which type the function predicted, as the index of the highest score"""
    max_val = None
    best_type = None
    type = 0
    # The score matrix is 1 x K; nodes lie in first row
    for score_node in self.score_nodes[0]:
      val = score_node.value()
      if max_val is None or max_val < val:
        max_val = val
        best_type = type
      type += 1
    return best_type


  def define_matrices(self):
    """Define matrices containing the layers, data inputs, and cost"""
    data_dim = 3  # includes bias value, always 1.0
    self.data = mat(data_dim,[0,0,1])
    self.data_type = mat(1,np.zeros(1))
    self.cost = mat(1,[0])
    self.w1 = np.random.randn(data_dim, NET_SIZE)
    self.w2 = np.random.randn(NET_SIZE, NUM_CLASSES)


  def define_function(self):
    f = Func()

    f.add_data("d",self.data)
    f.add_data("y",self.data_type)
    f.add_input("w1",self.w1)
    f.add_input("w2",self.w2)

    f.add_output("f",self.cost)

    # Generate matrix record for multiplication
    f.mult_matrix("d","w1","l1");

    # Generate nodes representing ReLU activation of a set of nodes
    f.relu_matrix("l1","relu")

    s = f.mult_matrix("relu","w2","s")

    self.score_nodes = s.get_nodes()

    svm_node = f.svm_loss(f.elem("y",0), self.score_nodes)
    reg_node = f.reg_loss("relu",0.1)
    f.connect(f.add(svm_node, reg_node),f.elem("f"))

    f.prepare()
    self.f = f


  def set_input(self,data):
    """Set the function input to a particular point"""
    x,y = data
    self.data[0,0] = x
    self.data[0,1] = y


  def perform_gradient_descent(self):
    f = self.f

    done = False

    reps = 0
    while not done:
      speed = math.pow(2.0, -(reps/30.0))

      # Iterate over all the training samples, plugging each into the function
      # and summing the cost and gradients produced
      num_samples = len(self.train_samples)
      gradient_sum_w1 = np.zeros_like(f.get_gradient("w1"))
      gradient_sum_w2 = np.zeros_like(f.get_gradient("w2"))
      cost_sum = 0

      for train_index in range(num_samples):
        train_sample = self.train_samples[train_index]
        self.set_input(train_sample)

        self.data_type[0] = self.train_types[train_index]

        f.evaluate()
        gradient_sum_w1 += f.get_gradient("w1")
        gradient_sum_w2 += f.get_gradient("w2")

        current_cost = self.cost.item((0,0))
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

      if reps == 75:
        done = True

      if reps > 10:
        if abs(current_cost - previous_cost) < 1e-7:
          done = True
          break

      previous_cost = current_cost

      m = f.get_matrix("w1").matrix()
      m += (-speed) * gradient_sum_w1
      m = f.get_matrix("w2").matrix()
      m += (-speed) * gradient_sum_w2

      if NET_SIZE <= 20:
        print "Trained w1:"
        print dm(f.get_matrix("w1").matrix())
        print "Trained w2:"
        print dm(f.get_matrix("w2").matrix())
        if reps == 12:
          f.make_dotfile()

  def evaluate_accuracy(self):
    """Determine accuracy of function relative to training set"""
    correct_count = 0
    n_samples = len(self.train_samples)
    for i in range(n_samples):
      self.set_input(self.train_samples[i])
      self.f.evaluate()
      eval_type = self.calculated_type()
      if self.train_types[i] == eval_type:
        correct_count += 1
    print "Accuracy:",df(correct_count / float(n_samples))


  def apply_function_to_grid(self):
    """Evaluate learned function for grid of points"""
    results = []
    for i in range(NUM_CLASSES):
      results.append([[],[]])

    res = 70
    for yi in range(res):
      y = 2 * (yi - res/2) / float(res)
      for xi in range(res):
        x = 2 * (xi - res/2) / float(res)
        self.set_input([x,y])
        self.f.evaluate()
        ls = results[self.calculated_type()]
        ls[0].append(x)
        ls[1].append(y)
    self.grid_results = results


  def plot_grid_results(self):
    type = 0
    colors = ['mo','yo','co']
    for ls in self.grid_results:
      plt.plot(ls[0],ls[1],colors[type])
      type += 1


  def plot_train_samples(self):
    colors2 = ['r.','g.','b.']
    for train_index in range(len(self.train_samples)):
      train_sample = self.train_samples[train_index]
      x = train_sample[0]
      y = train_sample[1]
      plt.plot(x,y,colors2[self.train_types[train_index]])



App().run()
