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


# INSERTION INTO ARRAY - Using array module
my_array1 = array.array('i', [1, 2, 3, 4])
print(my_array1)
my_array1.insert(2, 6)
print(my_array1)




# TRAVERSAL OF AN ARRAY
from array import *
arr1 = array('i', [1, 2, 3, 4, 5])
arr2 = array('d', [1.3, 1.5, 1.7])
def traverArray(arr):
    for i in arr:
        print(i)
traverArray(arr1)
traverArray(arr2)


# Accessing an element
from array import *
arr1 = array('i', [1, 2, 3, 4, 5, 6])
def accessElement(arr, index):
    if index < len(arr):
        return -1
    return arr[index]
accessElement(arr1, 4)


# Searching an element
from array import *
arr1 = array('i', [1, 2, 3, 4, 5, 6])
def searchElement(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return arr[i]
    return -1
searchElement(arr1, 4)