'''
Print all the duplicate characters in a string
Last Updated : 30 Jul, 2024
Given a string S, the task is to print all the duplicate characters 
    with their occurrences in the given string.

Example:

Input: S = “geeksforgeeks”
Output:
e, count = 4
g, count = 2
k, count = 2
s, count = 2

Explanation: g occurs 2 times in the string, k occurs 2 times in the string, 
    s occurs 2 times in the string while e occurs 4 times in the string 
    rest of the characters have unique occurrences.
'''

# Solution1 -   T - O(N), S - O(N)
def duplicate(input):
    dups = {}
    for char in input:
        if char not in dups:
            dups[char] = 1
        else:
            dups[char] += 1
    
    for key,count in dups.items():
        if count > 1:
            print(str(key) + " : " + str(count))

input = "geeksforgeeks"
duplicate(input)