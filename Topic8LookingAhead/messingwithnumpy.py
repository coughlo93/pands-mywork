# Messing with Numpy
# AUthor: Owen Coughlan

import numpy as np  

list_of_numbers= [1,2.3,"asdf"]
list_of_numbers = list_of_numbers + [3]
print (list_of_numbers)

numbers = np.array([1,2,3,4])
numbers = numbers * [1,2,3,5]

print(numbers)


#print random numbers
rando = np.random.randint(100,200,30)
print(rando)

normalrando = np.random.normal(loc = 50, scale= 20, size = 100)
print(normalrando)

