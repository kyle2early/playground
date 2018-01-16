# learning input and output
import numpy as np
import pickle
import json
from numpy import pi

## open deals with strings ONLY

f = open('workfile.txt', 'w')
f.write('this is a test file \n')
f.write("This is a new line \n")
f.write("this is another line \n")

f.close()

# reading contents of file
f = open('workfile.txt', 'r')

#f.read()
#f.readline() #reads a single line from workfile

#clost the file after you're done to free up resources
f.close()

## a smart way to deal with files, use with- it auto closes after finish
withk open('workfile.txt', 'r') as f:
    read_data = f.read()

# creating multidimensional array
data = np.arange(15).reshape(3,5)**3
print(data)


with open("workfile.txt", "a") as f:
    f.write(str(data) + "\n")

data = np.linspace(0, 2, 9)     #9 numbers from 0 to 2
print(data)

data = np.linspace(0, 2*pi, 100)
f = np.sin(data)


## to deal with numbers, use JSON (Javascript Object Notation)
