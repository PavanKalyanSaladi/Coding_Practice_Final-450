'''
Minimize the Heights I
Difficulty: MediumAccuracy: 26.16%Submissions: 70K+Points: 4
Given an array arr[] denoting heights of N towers and a positive integer K, you have to modify the height of each tower either by increasing or decreasing them by K only once.
Find out what could be the possible minimum difference of the height of shortest and longest towers after you have modified each tower.
Note: Assume that height of the tower can be negative.
A slight modification of the problem can be found here. 


Example 1:

Input:
K = 2, N = 4
Arr[] = {1, 5, 8, 10}
Output:
5
Explanation:
The array can be modified as 
{3, 3, 6, 8}. The difference between 
the largest and the smallest is 8-3 = 5.
Example 2:

Input:
K = 3, N = 5
Arr[] = {3, 9, 12, 16, 20}
Output:
11
Explanation:
The array can be modified as
{6, 12, 9, 13, 17}. The difference between 
the largest and the smallest is 17-6 = 11. 

Your Task:
You don't need to read input or print anything. Your task is to complete the function getMinDiff() which takes the arr[], n and k as input parameters and returns an integer denoting the minimum difference.


Expected Time Complexity: O(N*logN)
Expected Auxiliary Space: O(N)

Constraints
1 ≤ K ≤ 104
1 ≤ N ≤ 105
1 ≤ Arr[i] ≤ 105
'''

def getMinDiff(arr, n, k):
    arr.sort()
    ans = arr[n - 1] - arr[0]  # Maximum possible height difference
 
    tempmin = arr[0]
    tempmax = arr[n - 1]
 
    for i in range(1, n):
        if arr[i] < k:
            continue
        tempmin = min(arr[0] + k, arr[i] - k)
 
        # Minimum element when we
        # add k to whole array
        # Maximum element when we
        tempmax = max(arr[i - 1] + k, arr[n - 1] - k)
 
        # subtract k from whole array
        ans = min(ans, tempmax - tempmin)
 
    return ans
 
 
# Driver Code Starts
k = 6
n = 6
arr = [7, 4, 8, 8, 8, 9]
ans = getMinDiff(arr, n, k)
print(ans)

# Driver Code Starts
k = 3
n = 5
arr = [3, 9, 12, 16, 20]
ans = getMinDiff(arr, n, k)
print(ans)