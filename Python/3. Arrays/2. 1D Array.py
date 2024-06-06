# array module  - Python Standard library, no installation needed
import array
my_array = array.array('i')     # Stores the data as of no elements
print(my_array)
my_array1 = array.array('i', [1, 2, 3, 4])  # Only same type of elements can be stored
print(my_array1)

# numpy module  - Installation needs to be done before running
import numpy as np
np_array = np.array([],dtype=int)    # int type of empty array
print(np_array)
np_array1 = np.array([1, 2, 3, 4])
print(np_array1)



# INSERTION INTO ARRAY
# Using array module
my_array1 = array.array('i', [1, 2, 3, 4])
print(my_array1)
my_array1.insert(0, 6)
print(my_array1)