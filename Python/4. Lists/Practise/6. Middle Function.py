'''
Middle Function
Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

myList = [1, 2, 3, 4]
middle(myList)  # [2,3]
'''

def middle(lst):
    # TODO
    n = len(lst) - 1
    return lst[1:n]

print(middle([1, 2, 3, 4, 5, 6, 7]))