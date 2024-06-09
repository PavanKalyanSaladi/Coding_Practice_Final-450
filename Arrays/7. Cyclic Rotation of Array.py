'''
Cyclically rotate an array by one
BasicAccuracy: 69.6%Submissions: 260K+Points: 1
Solve right now
Given an array, rotate the array by one position in clock-wise direction.
 

Example 1:

Input:
N = 5
A[] = {1, 2, 3, 4, 5}
Output:
5 1 2 3 4
 

Example 2:

Input:
N = 8
A[] = {9, 8, 7, 6, 4, 2, 1, 3}
Output:
3 9 8 7 6 4 2 1

Your Task:  
You don't need to read input or print anything. Your task is to complete the function rotate() which takes the array A[] and its size N as inputs and modify the array in place.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1<=N<=105
0<=a[i]<=105
'''

# Method - 1, inbuilt functions
def rotate(arr):
    arr.insert(0, arr[len(arr) - 1])
    arr.pop()
    return arr

from array import *
arr = array('i', [1, 2, 3, 4, 5])
print(rotate(arr))


# Method - 2, For loop
def rotate1(arr, n):
    for i in range(n):
        arr[i],arr[n-1]=arr[n-1],arr[i]
    return arr

from array import *
arr = array('i', [1, 2, 3, 4, 5])
print(rotate1(arr, 5))