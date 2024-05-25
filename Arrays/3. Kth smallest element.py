'''

K'th Smallest/Largest Element in Unsorted Array | Expected Linear Time
Last Updated : 18 Sep, 2023
Prerequisite: K'th Smallest/Largest Element in Unsorted Array | Set 1

Given an array and a number k where k is smaller than the size of the array, 
we need to find the k'th smallest element in the given array. It is given that all array elements are distinct.

Examples:

Input: arr[] = {7, 10, 4, 3, 20, 15}
       k = 3
Output: 7



Input: arr[] = {7, 10, 4, 3, 20, 15}
      k = 4
Output: 10

We have discussed three different solutions here.

'''


# Appraoch 1
'''
K'th smallest element in an unsorted array using Sorting:
Sort the given array and return the element at index K-1 in the sorted array. 

Sort the input array in the increasing order
Return the element at the K-1 index (0 - Based indexing) in the sorted array
Below is the Implementation of the above approach:
'''

def kthLeastElement(arr, k):
    arr.sort()
    return arr[k - 1]

arr = [7, 10, 4, 3, 20, 15]
k = 4
print(kthLeastElement(arr, k))


# Approach 2