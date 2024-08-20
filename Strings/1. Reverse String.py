'''
Reverse String
Easy
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
'''

def reverse(s):
    # for i in range(len(s) // 2):
    #     s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]
    # return s

    # return s[:: -1]

    s.reverse()
    return s

s = ["h","e","l","l","o"]
print(reverse(s))