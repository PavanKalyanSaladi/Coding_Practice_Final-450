'''
Best Score
Given a list, write a function to get first, second best scores from the list.

List may contain duplicates.

Example

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
first_second(myList) # 90 87
'''

def first_second(my_list):
    # TODO
    first = 0
    second = -1
    for item in my_list:
        if item > first:
            second = first
            first = item
        elif item > second and item != first:
            second = item
    return first, second

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
print(first_second(myList))