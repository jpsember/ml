#! /usr/bin/env python

# Experiments with python and numpy, to determine how to
# represent and manipulate matrices

# See: https://docs.scipy.org/doc/numpy-dev/user/quickstart.html


import numpy as np
import math

# Defining a matrix

a = np.array([
    (0,1,2,3,4),
    (5,6,7,8,9),
    (10,11,12,13,14),
    ], dtype=float)

print a
print a.dtype

# Less verbose way of defining a matrix; avoid extra parenthese by using reshape:

a = np.array([
    0,1,2,3,4,
    5,6,7,8,9,
    10,11,12,13,14,
    ], dtype=float)
a = a.reshape(3,5)

print a

# Helper method to build array with implicit type, explicit # columns

def build_mat(ncols, arr):
  a = np.array(arr,dtype=float)
  a = a.reshape(a.size / ncols, ncols)
  return a

a = build_mat(5,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])
print a

