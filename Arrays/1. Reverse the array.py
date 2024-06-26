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
'''
Time Complexity: O(n)
    Copying elements to a new array is a linear operation.
Auxiliary Space Complexity: O(n)
    Additional space is used to store the new array.
'''
def reverseArray1(arr):
    rev = []
    for i in range(len(arr) - 1, -1, -1):
        rev.append(arr[i])
    return rev

print(reverseArray1([4, 5, 1, 2]))



# 2. Array Reverse Using a Loop (In-place):
'''
Time Complexity: O(n)
    The loop runs through half of the array, so it's linear with respect to the array size.
Auxiliary Space Complexity: O(1)
    In-place reversal, meaning it doesn't use additional space.
'''
def reverseArray2(arr):
    for i in range(len(arr) // 2):
        arr[i], arr[len(arr) - i - 1] = arr[len(arr) - i - 1], arr[i]
    return arr

print(reverseArray2([4, 5, 1, 2]))



# 3. Array Reverse Inbuilt Methods (Non In-place):
'''
Time Complexity: O(n)
    The loop runs through half of the array, so it's linear with respect to the array size.
Auxiliary Space Complexity: O(1)
    In-place reversal, meaning it doesn't use additional space.
'''
def reverseArray3(arr):
    return list(reversed(arr))

print(reverseArray3([4, 5, 1, 2]))



# 4. Array Reverse Recursion (In-place or Non In-place):
'''
Time Complexity: O(n)
    The loop runs through half of the array, so it's linear with respect to the array size.
Auxiliary Space Complexity: O(1)
    In-place reversal, meaning it doesn't use additional space.
'''
def reverseArray4(arr, start, end):
    if start >= end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverseArray4(arr, start + 1, end - 1)

arr = [4, 5, 1, 2]
reverseArray4(arr, 0, len(arr) - 1)
print(arr)



# 5. Array Reverse Stack (Non In-place):
'''
Time Complexity: O(n)
    Pushing and popping each element onto/from the stack requires linear time.
Auxiliary Space Complexity: O(n)
    Additional space is used to store the stack.
'''
def reverse_array_using_stack(arr):
    stack = []
    
    # Push elements onto the stack
    for element in arr:
        stack.append(element)
    
    # Pop elements from the stack to reverse the array
    for i in range(len(arr)):
        arr[i] = stack.pop()

    return arr

print(reverse_array_using_stack([4, 5, 1, 2]))