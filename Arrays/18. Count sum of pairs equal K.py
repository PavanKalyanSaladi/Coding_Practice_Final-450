'''
Count pairs with given sum
Last Updated : 08 Jul, 2024
Given an array of N integers, and an integer K, the task is to find the number of 
    pairs of integers in the array whose sum is equal to K.

Examples:  

Input: arr[] = {1, 5, 7, -1}, K = 6
Output:  2
Explanation: Pairs with sum 6 are (1, 5) and (7, -1).

Input: arr[] = {1, 5, 7, -1, 5}, K = 6
Output:  3
Explanation: Pairs with sum 6 are (1, 5), (7, -1) & (1, 5).         

Input: arr[] = {1, 1, 1, 1}, K = 2
Output:  6
Explanation: Pairs with sum 2 are (1, 1), (1, 1), (1, 1), (1, 1), (1, 1).

Input: arr[] = {10, 12, 10, 15, -1, 7, 6, 5, 4, 2, 1, 1, 1}, K = 11
Output:  9
Explanation: Pairs with sum 11 are (10, 1), (10, 1), 
    (10, 1), (12, -1), (10, 1), (10, 1), (10, 1), (7, 4), (6, 5).

Time Complexity: O(n), to iterate over the array
Auxiliary Space: O(n), to make a map of size n
'''

# Solution1 - Brute Force
def countPairs(arr, K):
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == K:
                count += 1
    return count

arr = [1, 5, 7, 1]
K = 6
print(countPairs(arr, K))


# Solution2 - Hashing
def countPairs2(arr, K):
    count = 0
    freq = {}

    for num in arr:
        if K - num in freq:
            count += freq[K - num]
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return count

arr = [1, 1, 1, 1]
K = 2
print(countPairs2(arr, K))