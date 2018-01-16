# plotting data using matplot
import numpy as np
import matplotlib.pyplot as plt

# line plot

year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.592, 5.263, 6.90]

plt.plot(year, pop)
plt.show()

# scatter plot
plt.scatter(year, pop)
plt.show()

# histogram; default bins are 10

x = [ 1, 2, 3, 4, 10, 20, 30, 40]
plt.hist(x)
plt.show()
plt.clf()

# specify the number of bins
plt.hist(x, bins = 3)
plt.show()

#customizing plots

# scatter plot
plt.scatter(year, pop)
plt.xlabel('Years')
plt.ylabel('Population [in Millions]')
plt.title('Population Change in Country "x"')

plt.show()
