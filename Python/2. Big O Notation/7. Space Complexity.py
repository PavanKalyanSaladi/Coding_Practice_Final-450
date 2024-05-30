''' 
Here the function calls itself and store the current result
in the stack and vise versa

Ex- n = 4
    sum(4)
        sum(3)
            sum(2)
                sum(1)
                    sum(0)

Note:- The last one pops first and the rest

Space Complexity: O(N)
'''
def sum(n):
    if n <=0:
        return 0
    return n + sum(n - 1)

print(sum(5))


'''
Print the sum of two values.
- Function is called with two values and return their sum.

Space Complexity: O(1)
Time Complexity: O(1)
'''
def sum(a, b):
    return a + b
print(sum(2, 3))