'''
Union of two arrays
BasicAccuracy: 42.22%Submissions: 355K+Points: 1
Be the comment of the day in POTD and win a GfG T-Shirt!
Solve right now

banner
Given two arrays a[] and b[] of size n and m respectively. The task is to find the number of elements in the union between these two arrays.

Union of the two arrays can be defined as the set containing distinct elements from both the arrays. If there are repetitions, then only one occurrence of element should be printed in the union.

Note : Elements are not necessarily distinct.

Example 1:

Input:
5 3
1 2 3 4 5
1 2 3
Output: 
5
Explanation: 
1, 2, 3, 4 and 5 are the
elements which comes in the union set
of both arrays. So count is 5.
Example 2:

Input:
6 2 
85 25 1 32 54 6
85 2 
Output: 
7
Explanation: 
85, 25, 1, 32, 54, 6, and
2 are the elements which comes in the
union set of both arrays. So count is 7.
Your Task:
Complete doUnion function that takes a, n, b, m as parameters and returns the count of union elements of the two arrays. The printing is done by the driver code.

Constraints:
1 ≤ n, m ≤ 105
0 ≤ a[i], b[i] < 105

Expected Time Complexity : O(n+m)
Expected Auxilliary Space : O(n+m)
'''

# 1. Using union    -   If inputs is set
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(len(z))

# 2. If input is array
from array import *
arr1 = array('i', [1, 2, 3, 4, 5])
arr2 = array('i', [1, 2, 3])
print(len(list(set(arr1 + arr2))))

# 3. using set.unions
from array import *
arr1 = array('i', [1, 2, 3, 4, 5])
arr2 = array('i', [1, 2, 3])
def unionOfAB(arr1, arr2):
    print(len(set(arr1).union(set(arr2))))
unionOfAB(arr1, arr2)
