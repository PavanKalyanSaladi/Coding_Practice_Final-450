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

Time Complexity: O(N log N)
Auxiliary Space: O(1) 
'''

def kthLeastElement(arr, k):
    arr.sort()
    return arr[k - 1]

arr = [7, 10, 4, 3, 20, 15]
k = 4
print("Using array.sort() ", kthLeastElement(arr, k))



# Approach 2
'''
Follow the given steps to solve the problem:

Intialize low and high to minimum and maximum element of the array 
    denoting the range within which the answer lies.
Apply Binary Search on this range. 
If the selected element by calculating mid has less than K elements 
    lesser to it then increase the number that is low = mid + 1.
Otherwise, Decrement the high pointer, i.e high = mid.
The Binary Search will end when only one element remains in the answer
    space that would be the answer.

Time complexity: O(n * log (mx-mn)), where mn be minimum and mx be maximum element of array.
Auxiliary Space: O(1)
'''

def count(arr, mid):
    cnt = 0
    for i in range(len(arr)):
        if arr[i] <= mid:
            cnt += 1
    return cnt
 
 
def kthLeastBinarySearch(arr, k):
    # calculate minimum and maximum the array.
    low = min(arr)
    high = max(arr)
    
    # Our answer range lies between minimum and maximum element
    # of the array on which Binary Search is Applied
    while low < high:
        mid = low + (high - low) // 2
        # if the count of number of elements in the array less than equal
        # to mid is less than k then increase the number. Otherwise decrement
        # the number and try to find a better answer.
        if count(arr, mid) < k:
            low = mid + 1
        else:
            high = mid
    return low

arr = [7, 10, 4, 3, 20, 15]
k = 4
print("Using Binary Search ", kthLeastElement(arr, k))


# Approach 3
