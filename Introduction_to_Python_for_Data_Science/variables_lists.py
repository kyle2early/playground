family = ["john", "kate", "josh", "lily","diane"]
print(family)
print(type(family))

# Lists within lists
family2 = [[family[0], 24], [family[1], 13], [family[2], 18], [family[3], 0], [family[4], 36]]
print(family2)
print(type(family2))

# Difference between single & double quotes
x = ['k', "k"]
print(x)
print(type(x))

# Indexing and slicing data
# Select begining of list until index location (excludes index loation value)
print(family[:2])

 # Select some index to end of list
print(family[1:])

# Manipulating lists is funky! copying a list doesnt copy data- just references it

print(family)
y = family
print(y)
y[0] = "Johnathan"
print(y)
print(family) # Pretty freaky, yea!

# You can modify list- adding
family2 = family2 + [["Timmy, 3"]]
print(family2)
family2.append(["Jane",3])
print(family2)

# removing items
family2.remove(["Jane", 3])
print(family2)

# delete item from list given its Index
del family2[0]
print(family2)

# where is kate located in the list
print(family)
print(family.index("kate"))

# to print out length of lists & variables
print(len(family2))
