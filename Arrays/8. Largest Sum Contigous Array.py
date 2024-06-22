'''
Kadane's Algorithm
Difficulty: MediumAccuracy: 36.28%Submissions: 912K+Points: 4
Given an array arr[] of n integers. Find the contiguous sub-array
(containing at least one number) which has the maximum sum and return its sum.

Examples:

Input: arr[] = {1,2,3,-2,5}, n = 5
Output: 9
Explanation: Max subarray sum is 9 of elements (1, 2, 3, -2, 5) which is a contiguous subarray.

Input: arr[] = {-1,-2,-3,-4}, n = 4
Output: -1
Explanation: Max subarray sum is -1 of element (-1)

Input: arr[] = {5,4,7}, n = 3
Output: 16
Explanation: Max subarray sum is 16 of element (5, 4, 7)

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
-107 ≤ arr[i] ≤ 107
1 ≤ n ≤ 106
'''

def maxSubArray(arr):
    if not arr:
        return 0
    
    current_sum = arr[0]
    max_sum = arr[0]
    
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
        
    return max_sum

arr = [-1, -2, -3, -4]
print(maxSubArray(arr))

'''
Explanation of the Implementation:
current_sum starts with the first element arr[0] because it represents 
    the maximum subarray sum ending at the first element.
max_sum also starts with arr[0] as it is the maximum sum found so far.
Iterate through the array starting from the second element (arr[1:]).
For each element, update current_sum to the maximum of the current element
    alone or the sum of current_sum + num.
Update max_sum to be the maximum of itself and current_sum after each iteration.
'''