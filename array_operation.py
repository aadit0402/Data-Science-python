# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 18:57:32 2017

@author: aditya
"""

import numpy as np

n_array = np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11]])

print "output:2 indicate 2d array", n_array.ndim

print "output:(3,4) shape of array", n_array.shape

print "output:size of array 12", n_array.size

print "output:datatype of the elements in the array: int64", n_array.dtype.name

print "Mathematical Operation"

print "array subtraction"

a = np.array([11,12,13,14])
b = np.array([1,2,3,4])

print a-b

print "squaring array"

print b**2;

print "trigonometric function performed on array"
print np.cos(b)

print "conditional operation", b<2

print "multiplication of a and b",a * b

print "dot product of a and b",np.dot(a, b)

print "indexing and slicing:"

print n_array[0, :] #first row of value
print n_array[1, 0:4] #second row of value
print n_array[2, 0:4] #third row of value
#print n_array[3, 0:4] // error index 3 is out of bound for axis 0 with size 3 when we try to access the data beyond the array
print n_array[:, 1] # first column of the array

print "shape manipulation"
print n_array.ravel() #it will change the shape of the array; flatten the array

n_array.shape = (6,2) # change the shape to 6 by 2 from 3 by 4
print  n_array

print n_array.transpose() #transpose of array