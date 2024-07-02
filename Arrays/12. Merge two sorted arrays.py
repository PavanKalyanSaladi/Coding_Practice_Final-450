'''
Merge two sorted arrays
Last Updated : 03 Oct, 2023
 
Given two sorted arrays, the task is to merge them in a sorted manner.
Examples: 

Input: arr1[] = { 1, 3, 4, 5}, arr2[] = {2, 4, 6, 8} 
Output: arr3[] = {1, 2, 3, 4, 4, 5, 6, 8}

Input: arr1[] = { 5, 8, 9}, arr2[] = {4, 7, 8} 
Output: arr3[] = {4, 5, 7, 8, 8, 9} 
'''

# Extra Space used

def mergeArrays(arr1, arr2, n1, n2):
    arr3 = [None] * (n1 + n2)
    i = 0
    j = 0
    k = 0
 
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            k = k + 1
            i = i + 1
        else:
            arr3[k] = arr2[j]
            k = k + 1
            j = j + 1
    
    while i < n1:
        arr3[k] = arr1[i]
        k = k + 1
        i = i + 1
    
    while j < n2:
        arr3[k] = arr2[j]
        k = k + 1
        j = j + 1
    
    print("Array after merging")
    for i in range(n1 + n2):
        print(str(arr3[i]), end = " ")
 
# Driver code
arr1 = [1, 3, 5, 7]
n1 = len(arr1)
 
arr2 = [2, 4, 6, 8]
n2 = len(arr2)
mergeArrays(arr1, arr2, n1, n2)



# Without extra space

def merge(ar1, ar2, m, n):

    # Iterate through all
    # elements of ar2[] starting from
    # the last element
    for i in range(n-1, -1, -1):

        # Find the smallest element
        # greater than ar2[i]. Move all
        # elements one position ahead
        # till the smallest greater
        # element is not found
        last = ar1[m-1]
        j = m-2
        while(j >= 0 and ar1[j] > ar2[i]):
            ar1[j+1] = ar1[j]
            j -= 1

        # If there was a greater element
        if (last > ar2[i]):

            ar1[j+1] = ar2[i]
            ar2[i] = last

# Driver code
ar1 = [1, 5, 9, 10, 15, 20]
ar2 = [2, 3, 8, 13]
m = len(ar1)
n = len(ar2)

merge(ar1, ar2, m, n)

print("\nAfter Merging :")
for i in range(m):
    print(ar1[i], end=" ")

for i in range(n):
    print(ar2[i], end=" ")