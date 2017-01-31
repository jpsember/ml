# Common functions for neural (spiral) program

import numpy as np
import math
from tools import *

NUM_CLASSES = 3

def build_spiral_data(points_per_class = 100, num_classes = NUM_CLASSES):
  X = np.zeros((points_per_class*num_classes,2)) # data matrix (each row = single example)
  y = np.zeros(points_per_class*num_classes, dtype='uint8') # class labels
  for j in xrange(num_classes):
    ix = range(points_per_class*j,points_per_class*(j+1))
    r = np.linspace(0.0,1,points_per_class)
    t = np.linspace(j*4,(j+1)*4,points_per_class) + np.random.randn(points_per_class)*0.2 # theta
    X[ix] = np.c_[r*np.sin(t), r*np.cos(t)]
    y[ix] = j
  return (X,y)


