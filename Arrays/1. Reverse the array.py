'''
Array reverse or reverse a array means changing the 
position of each number of the given array to its 
opposite position from end, i.e. if a number is at 
position 1 then its new position will be Array.length,
similarly if a number is at position 2 then its 
new position will be Array.length - 1, and so on.

Given an array (or string), the task is to reverse the array/string.

Examples:

Input: original_array[] = {1, 2, 3} Output: array_reversed[] = {3, 2, 1}


Input: original_array[] = {4, 5, 1, 2}
Output: array_reversed[] = {2, 1, 5, 4}

Table of Content

1. Array Reverse Using an Extra Array (Non In-place):
2. Array Reverse Using a Loop (In-place):
3. Array Reverse Inbuilt Methods (Non In-place):
4. Array Reverse Recursion (In-place or Non In-place):
5. Array Reverse Stack (Non In-place):

'''

# 1. Array Reverse Using an Extra Array (Non In-place):

def reverseArray1(arr):
    rev = []
    for i in range(len(arr) - 1, -1, -1):
        rev.append(arr[i])
    return rev

print(reverseArray1([4, 5, 1, 2]))


# 2. Array Reverse Using a Loop (In-place):

def reverseArray2(arr):
    for i in range(len(arr) // 2):
        arr[i], arr[len(arr) - i - 1] = arr[len(arr) - i - 1], arr[i]
    return arr

print(reverseArray2([4, 5, 1, 2]))


# 3. Array Reverse Inbuilt Methods (Non In-place):

def reverseArray3(arr):
    return list(reversed(arr))

print(reverseArray3([4, 5, 1, 2]))