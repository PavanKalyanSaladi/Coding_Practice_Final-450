'''
Common in 3 Sorted Arrays

You are given three arrays sorted in increasing order. 
Find the elements that are common in all three arrays.
If there are no such elements return an empty array. In this case, the output will be -1.

Note: can you handle the duplicates without using any additional Data Structure?

Examples :

Input: arr1 = [1, 5, 10, 20, 40, 80] , arr2 = [6, 7, 20, 80, 100] , 
    arr3 = [3, 4, 15, 20, 30, 70, 80, 120]
Output: [20, 80]
Explanation: 20 and 80 are the only common elements in arr, brr and crr.
Input: arr1 = [1, 2, 3, 4, 5] , arr2 = [6, 7] , arr3 = [8,9,10]
Output: [-1]
Explanation: There are no common elements in arr, brr and crr.
Input: arr1 = [1, 1, 1, 2, 2, 2], B = [1, 1, 2, 2, 2], arr3 = [1, 1, 1, 1, 2, 2, 2, 2]
Output: [1, 2]
Explanation: We do not need to consider duplicates
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Here n = Total sizes of arr1, arr2, and arr3

Constraints:
1 <= arr1.size(), arr2.size(), arr3.size() <= 105
-105 <= arr1i , arr2i , 1arr3i <= 105
'''

def commoninthree(arr1, arr2, arr3):
    len1 = len(arr1)
    len2 = len(arr2)
    len3 = len(arr3)

    i, j, k = 0, 0, 0

    common = set()

    while i < len1 or j < len2 or k < len3:
        if i == len1 or j == len2 or k == len3:
            if common == ():
                return [-1]
            return sorted(common)
        if arr1[i] == arr2[j] and arr1[i] == arr3[k]:
            common.add(arr1[i])
        if arr1[i] < arr2[j]:
            if arr1[i] < arr3[k]:
                i += 1
            else:
                k += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1
    return sorted(common)

arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]
print(commoninthree(arr1, arr2, arr3))