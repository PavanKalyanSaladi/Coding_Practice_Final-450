'''
Move all negative numbers to beginning and positive to end with constant extra space
Last Updated : 29 Apr, 2024
An arr1ay contains both positive and negative numbers in random order. Rearr1ange the arr1ay elements so that all negative numbers appear before all positive numbers.

Examples : 

Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
Output: -12 -13 -5 -7 -3 -6 11 6 5

Note: Order of elements is not important here.
'''

# 1. O(NlogN) - Time, O(1) - Space
arr1 = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
arr1.sort()
print(arr1)

# 2. O(N) - Time, O(1) - Space
def moveNegPos(arr1):
    i = 0
    j = 0
    while j < len(arr1):
        if arr1[j] < 0:
            arr1[i], arr1[j] = arr1[j], arr1[i]
            i += 1
        j += 1
    print(arr1)

arr1 = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
moveNegPos(arr1)