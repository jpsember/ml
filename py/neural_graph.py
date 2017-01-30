#! /usr/bin/env python

# Represent a neural network as a graph,
# train it to assign colors to the 'spiral' points
#

import numpy as np
import math
from func import *
from common import *

TWO_LAYERS = False

# Size of hidden layer
if TWO_LAYERS:
  NET_SIZE = 10
else:
  NET_SIZE = 100

class App:


  def run(self):
    np.random.seed(1965)
    self.train_samples,self.train_types = build_spiral_data(100,NUM_CLASSES)
    self.define_matrices()
    self.define_function()
    self.perform_gradient_descent()
    self.evaluate_accuracy()
    self.apply_function_to_grid()
    self.plot_grid_results()
    self.plot_train_samples()
    save_plot()


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
    if TWO_LAYERS:
      self.w2 = np.random.randn(NET_SIZE,NET_SIZE)
    self.w_out = np.random.randn(NET_SIZE, NUM_CLASSES)


  def define_function(self):
    f = Func()

    f.add_data("d",self.data)
    f.add_data("y",self.data_type)
    f.add_input("w1",self.w1)
    if TWO_LAYERS:
      f.add_input("w2",self.w2)
    f.add_input("w_out",self.w_out)

    f.add_output("f",self.cost)

    f.mult_matrix("d","w1","l1");
    f.relu_matrix("l1","r1")
    r_out = "r1"

    if TWO_LAYERS:
      f.mult_matrix("r1","w2","l1b")
      f.relu_matrix("l1b","r2")
      r_out = "r2"

    s = f.mult_matrix(r_out,"w_out","s")

    self.score_nodes = s.get_nodes()

    svm_node = f.svm_loss(f.elem("y",0), self.score_nodes)

    # We don't need reg loss on relu matrices, since they are already proportional to the matrices they follow
    nodes = [svm_node]
    if TWO_LAYERS:
      wt = 0.1 / 3
      nodes.append(f.reg_loss("w1",wt))
      nodes.append(f.reg_loss("w2",wt))
      nodes.append(f.reg_loss("w_out",wt))
    else:
      wt = 0.1 / 2
      nodes.append(f.reg_loss("w1",wt))
      nodes.append(f.reg_loss("w_out",wt))

    f.connect(f.add(*nodes),f.elem("f"))

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
      if TWO_LAYERS:
        gradient_sum_w1b = np.zeros_like(f.get_gradient("w2"))
      gradient_sum_w2 = np.zeros_like(f.get_gradient("w_out"))
      cost_sum = 0

      for train_index in range(num_samples):
        train_sample = self.train_samples[train_index]
        self.set_input(train_sample)

        self.data_type[0] = self.train_types[train_index]

        f.evaluate()
        gradient_sum_w1 += f.get_gradient("w1")
        if TWO_LAYERS:
          gradient_sum_w1b += f.get_gradient("w2")
        gradient_sum_w2 += f.get_gradient("w_out")

        current_cost = self.cost.item((0,0))
        cost_sum += current_cost

      # Replace cost/gradient sums with averages
      current_cost = cost_sum / num_samples
      gradient_sum_w1 *= (1.0 / num_samples)
      if TWO_LAYERS:
        gradient_sum_w1b *= (1.0 / num_samples)
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
      if TWO_LAYERS:
        m = f.get_matrix("w2").matrix()
        m += (-speed) * gradient_sum_w1b
      m = f.get_matrix("w_out").matrix()
      m += (-speed) * gradient_sum_w2

      if NET_SIZE <= 20:
        self.display_parameters()
        if reps == 12:
          f.make_dotfile()

    self.display_parameters()


  def display_parameters(self):
    f = self.f
    print "Trained w1:"
    print dm(f.get_matrix("w1").matrix())
    if TWO_LAYERS:
      print "Trained w1b:"
      print dm(f.get_matrix("w2").matrix())
    print "Trained w2:"
    print dm(f.get_matrix("w_out").matrix())

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
