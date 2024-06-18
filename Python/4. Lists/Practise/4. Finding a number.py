'''
Finding a number in an array

input:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
10

output:
True
'''

# If input is list
def findNumber(arr, value):
    return value in arr

print(findNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 10))


# If input is array
def linear_search(arr, value):
    for num in arr:
        if num == value:
            return True
    return False

from array import *                                                     # method 1
arr = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
import numpy as np                                                      # method 2
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
print(linear_search(arr, 12))