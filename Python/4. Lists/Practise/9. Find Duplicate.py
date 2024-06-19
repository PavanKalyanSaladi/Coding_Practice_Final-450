'''
Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example :

Input: nums = [1,2,3,1]
Output: true
Hint: Use sets
'''

def duplicate(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False

print(duplicate([1,2,3,1]))