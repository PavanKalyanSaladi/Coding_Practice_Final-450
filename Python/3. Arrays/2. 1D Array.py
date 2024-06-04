# array module  - Python Standard library, no installation needed
import array
my_array = array.array('i')     # Stores the data as of no elements
print(my_array)
my_array1 = array.array('i', [1, 2, 3, 4])  # Only same type of elements can be stored
print(my_array1)


# numpy module  - Installation needs to be done before running
import numpy as np