#! /usr/bin/env python

# Represent a neural network using numpy;
# train it to assign colors to the 'spiral' points
#

import numpy as np
import math
from common import *


class App:


  def run(self):
    np.random.seed(1965)
    self.train_samples,self.train_types = build_spiral_data(100,NUM_CLASSES)



App().run()
