'''
Given an array A[] consisting of only 0s, 1s, and 2s. 
The task is to write a function that sorts the given array. 
The functions should put all 0s first, then all 1s and all 2s in last.

This problem is also the same as the famous “Dutch National Flag problem”.
The problem was proposed by Edsger Dijkstra. The problem is as follows:

Given N balls of colour red, white or blue arranged in a line in random order.
You have to arrange all the balls such that the balls with the same colours 
are adjacent with the order of the balls, with the order of the colours being
red, white and blue (i.e., all red coloured balls come first then the white 
coloured balls and then the blue coloured balls). 

Examples:

Input: {0, 1, 2, 0, 1, 2}
Output: {0, 0, 1, 1, 2, 2}

Input: {0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1}
Output: {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2}
'''


# Approach1
'''
Sort an array of 0s, 1s, and 2s using the Pointer Approach: 
This approach is based on the following idea:

The problem is similar to “Segregate 0s and 1s in an array”.
The problem was posed with three colors, here '0', '1' and '2'. 
The array is divided into four sections: 
arr[1] to arr[low - 1]
arr[low] to arr[mid - 1]
arr[mid] to arr[high - 1]
arr[high] to arr[n]
If the ith element is 0 then swap the element to the low range.
Similarly, if the element is 1 then keep it as it is.
If the element is 2 then swap it with an element in high range.
'''
def sortNumbers(arr):
    low = 0
    mid = 0
    high = len(arr) - 1
    for i in range(len(arr)):
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        elif arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
        else:
            print("Given array consists of non-input value.")
            exit(0)
    return arr

arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
print(sortNumbers(arr))