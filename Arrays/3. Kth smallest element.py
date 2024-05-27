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
print("Using Binary Search ", kthLeastBinarySearch(arr, k))



# Approach 3
'''
Follow the given steps to solve the problem:

Run quick sort algorithm on the input array
In this algorithm pick a pivot element and move it to it's correct position
Now, if index of pivot is equal to K then return the value, else if the index of pivot is greater than K, then recur for the left subarray, else recur for the right subarray 
Repeat this process until the element at index K is not found

Time Complexity: O(N2) in worst case and O(N) on average. 
    However if we randomly choose pivots, the probability of worst case could become very less.
Auxiliary Space: O(N)
'''
import sys

def kthSmallestQuickSort(arr, l, r, K):
 
    # If k is smaller than number of
    # elements in array
    if (K > 0 and K <= r - l + 1):
 
        # Partition the array around last
        # element and get position of pivot
        # element in sorted array
        pos = partition(arr, l, r)
 
        # If position is same as k
        if (pos - l == K - 1):
            return arr[pos]
        if (pos - l > K - 1):  # If position is more,
                              # recur for left subarray
            return kthSmallestQuickSort(arr, l, pos - 1, K)
 
        # Else recur for right subarray
        return kthSmallestQuickSort(arr, pos + 1, r,
                           K - pos + l - 1)
 
    # If k is more than number of
    # elements in array
    return sys.maxsize
 
# Standard partition process of QuickSort().
# It considers the last element as pivot and
# moves all smaller element to left of it
# and greater elements to right
 
def partition(arr, l, r):
 
    x = arr[r]
    i = l
    for j in range(l, r):
        if (arr[j] <= x):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i

arr = [7, 10, 4, 3, 20, 15]
n = len(arr)
k = 4
print("Using Quick Sort ", kthSmallestQuickSort(arr, 0, n-1, k))