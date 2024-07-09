'''
Count Inversions
Difficulty: MediumAccuracy: 16.93%Submissions: 517K+Points: 4
Given an array of integers. Find the Inversion Count in the array.  Two array elements arr[i] and arr[j] form an inversion if arr[i] > arr[j] and i < j.

Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If the array is already sorted then the inversion count is 0.
If an array is sorted in the reverse order then the inversion count is the maximum. 

Examples:

Input: n = 5, arr[] = {2, 4, 1, 3, 5}
Output: 3
Explanation: The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).
Input: n = 5, arr[] = {2, 3, 4, 5, 6}
Output: 0
Explanation: As the sequence is already sorted so there is no inversion count.
Input: n = 3, arr[] = {10, 10, 10}
Output: 0
Explanation: As all the elements of array are same, so there is no inversion count.
Expected Time Complexity: O(nLogn).
Expected Auxiliary Space: O(n).

Constraints:
1 ≤ n ≤ 5*105
1 ≤ arr[i] ≤ 1018
'''

def countInversions(arr):       # O(N^2) - Time Complexity
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                count += 1
    return count

arr = [2, 4, 1, 3, 5]
print(countInversions(arr))



def mergeSort(arr, n):          # O(NlogN) - Time Complexity

    # A temp_arr is created to store
    # sorted array in merge function
    temp_arr = [0]*n
    return _mergeSort(arr, temp_arr, 0, n-1)

# This Function will use MergeSort to count inversions

def _mergeSort(arr, temp_arr, left, right):

    # A variable inv_count is used to store
    # inversion counts in each recursive call

    inv_count = 0

    # We will make a recursive call if and only if
    # we have more than one elements

    if left < right:

        # mid is calculated to divide the array into two subarrays
        # Floor division is must in case of python

        mid = (left + right)//2

        # It will calculate inversion
        # counts in the left subarray

        inv_count += _mergeSort(arr, temp_arr,
                                left, mid)

        # It will calculate inversion
        # counts in right subarray

        inv_count += _mergeSort(arr, temp_arr,
                                mid + 1, right)

        # It will merge two subarrays in
        # a sorted subarray

        inv_count += merge(arr, temp_arr, left, mid, right)
    return inv_count

# This function will merge two subarrays
# in a single sorted subarray


def merge(arr, temp_arr, left, mid, right):
    i = left     # Starting index of left subarray
    j = mid + 1  # Starting index of right subarray
    k = left     # Starting index of to be sorted subarray
    inv_count = 0

    # Conditions are checked to make sure that
    # i and j don't exceed their
    # subarray limits.

    while i <= mid and j <= right:

        # There will be no inversion if arr[i] <= arr[j]

        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            # Inversion will occur.
            temp_arr[k] = arr[j]
            inv_count += (mid-i + 1)
            k += 1
            j += 1

    # Copy the remaining elements of left
    # subarray into temporary array
    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1

    # Copy the remaining elements of right
    # subarray into temporary array
    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1

    # Copy the sorted subarray into Original array
    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]

    return inv_count

arr = [1, 20, 6, 4, 5]
n = len(arr)
result = mergeSort(arr, n)
print("Number of inversions are", result)