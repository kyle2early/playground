#working with packages

import math

r = 1.2
C = 2*math.pi*r
print("circumference: " + str(round(C,3)))

# selective imports of functions from package

from math import pi

A = pi*r*r
print("Area: " + str(A))

# Numpy package: useful for data science- dealing with arrays &etc, vector arithmetics, items are HOMOGENOUS,
# "Numeric Python"
# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Import the numpy package as np
import numpy as np

# Create a Numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(np_baseball)
print(type(baseball))
print(type(np_baseball))

print(np_baseball[2:4]) # indexing works as normal

# working with arrays is insteresting
# find values less than 200
less_than_200 = np_baseball < 200
print(less_than_200)

# print the ACTUAL values
print(np_baseball[less_than_200])

# working with diff data types..

x = np.array([3, True, "string"])
print(type(x))
print(x)        # coerced data type- changes into to most general type, in this case "string"


## 2D Numpy arrays
baseball = [[180, 215, 210],
[210, 188, 176],
[209,200,300]]
np_baseball = np.array(baseball)

print(type(np_baseball))
print(np_baseball.shape)

# data statistics

print(np_baseball - [1, 2, 3])
print(np_baseball *  2)

# average of columns
np_mean = np.mean(np_baseball[:,0])
print(np_mean)
print("mean of column 1: " + str(np_mean))

print("median of column 1: " + str(np.median(np_baseball[:,0])))

np_mean = np.mean(np_baseball[:,2])
print("average of column 3: " + str(np_mean))

print("median of column 3: " + str(np.median(np_baseball[:,2])))

print("standard deviation, 3: " + str(np.std(np_baseball[0,:2])))

print("correlation 2 & 3 : " + str(np.corrcoef(np_baseball[:,1], np_baseball[:,2])))
