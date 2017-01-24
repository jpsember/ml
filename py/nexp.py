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

# Vector
v1 = np.array([1,2,3],dtype=float)
v2 = np.array([3,-1,1],dtype=float)


print v1
print v2

# Scalar product

print "dot(v1,v2): ",np.dot(v1,v2)
print "v1 * v2 (NOT the scalar product!):    ", v1 * v2

# Extract rows, columns as vectors
r = a[1]
print "second row: ",r

c = a[:,1]
print "second col: ",c

# Helper methods to extract rows or columns
# (is this a good idea, e.g., to have a level of abstraction above ndarray?)
def row(matrix, row_number):
  return matrix[row_number]

def col(matrix, col_number):
  return matrix[:,col_number]

print "third row:", row(a,2)
print "third col:", col(a,2)

print "scalar product of rows 0 and 2:", np.dot(row(a,0), row(a,2))

