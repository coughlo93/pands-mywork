import numpy as np
import matplotlib.pyplot as plt
minSalary = 20000
maxSalary = 80000
numberOfEntries = 100
# this is so that the "random" numbers are the same each time to make it easier to debug.

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
ages = np.random.randint(low=21, high = 65, size = numberOfEntries)
 
# I don’t like this, I prefer having absolute values set at the top
plt.scatter(ages, salaries ) # this will be random
plt.show()
