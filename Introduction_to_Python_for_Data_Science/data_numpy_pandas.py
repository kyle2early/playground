import numpy as np
import pandas as pd

# Numpy:  2D arrays of homogenous read_data

## 2D Numpy arrays
baseball = [[180, 215, 210],
[210, 188, 176],
[209,200,300]]
np_baseball = np.array(baseball)    #converts to array- easier manupulation
print(np_baseball)

#create array of 3x5
data = np.ones((3,5), dtype=int)
print(data)

# create array with exact number of elements needed
data = np.linspace(0,2,9)          # 9 numbers from 0 to 2
print(data)

# create array with sequence of numbers
data = np.arange(10,30,5)           #from 10 to 30, indexed by 5
print(data)

# Operations
A = np.array ([[1,1], [0,1]])
B = np.array ([[2,0], [3,4]])

print(A*B)          # Elementwise product

print(A.dot(B))     #matrix product

print(np.dot(A,B))

print(A*1.2)

print(A.sum())      #sum of all elements
print(A.sum(axis=0))
print(B.cumsum())

print(np.sqrt(B))

#Shape manupulation

A = np.floor(10*np.random.random((3,4)))
print(A.shape)
print(A)
print(A.ravel())      #flatens arrays

print(A.reshape(6,2))
print(A.T)      #transpose
print(A.shape)
## Splitting arrays

a = np.hsplit(A,2)      #split into 2 arrays
print(a)

a = np.hsplit(A,(1,3))          # split after 1st & 3th column
print(a)

# Copying & assignaments
a = np.array([1,2,3])
b = a
c = np.copy(b)


### Pandas for dataframe; typically imports from csv
cars = pd.read_csv("cars.csv", index_col = 0)
print(cars)
print(cars['country'])          # prints out as series
print(cars[['country']])        # prints out as dataframe

## data selection
print(cars.loc['US'])       #print as series
print(cars.loc[['US']])     #print as DataFrame
print(cars.loc[['US', 'EG']])
print(cars.loc['US', 'drives_right'])   #you can select column value

## modify dataframes s
