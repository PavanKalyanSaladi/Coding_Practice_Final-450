# 1. Create an array and traverse
from array import *
arr1 = array('i', [1, 2, 3, 4, 5, 6])
for i in range(len(arr1)):
    print(arr1[i], end=" ")
print()

# 2. Access individual elements through indexes
print(arr1[2])
print(arr1[4])

# 3. Append any value to the array using append() method
arr1.append(7)
print(arr1)

# 4. Insert value in an array using insert() method
arr1.insert(0, -1)
print(arr1)

# 5. Extend python array using extend() method
arr2 = array('i', [11, 12, 13])
arr1.extend(arr2)
print(arr1)

# 6. Add items from list into array using fromlist() method
arr1.fromlist([14, 15, 16])
print(arr1)

# 7. Remove any array element using remove() method
arr1.remove(-1)
print(arr1)

# 8. Remove last array element using pop() method
arr1.pop()
print(arr1)

# 9. Fetch any element through its index using index() method
print(arr1.index(5))

# 10. Reverse a python array using reverse() method
arr1.reverse()
print(arr1)

# 11. Get array buffer information through buffer_info() method
print(arr1.buffer_info())

# 12. Check for number of occurences of an element using count() method
print(arr1.count(1))

# 13. Convert array to string using to string() method
strTemp = arr1.tobytes()
print(strTemp)
'''
ints = array('i')
ints.frombytes(arr1)
print(ints)
'''

# 14. Convert array to a python list with same elements using tolist() method
print(arr1.tolist())

# 15. Append a string to char array using fromstring() method
# print(arr1.frombytes('str'))

# 16. Slice elements from an array
print(arr1[:])