'''
Traversing through a dictionary.

Time Complexity     : O(n)
Space Complexity    : O(1)
'''

my_Dict = {'name': 'Pavan', 'age': 23, 'address': 'hyderabad', 'education': 'masters'}

def searchDict(my_Dict, value):
    for key in my_Dict:
        if my_Dict[key] == value:
            return key, value
    return 'The value does not exist'

print(searchDict(my_Dict, 27))

print(searchDict(my_Dict, 'masters'))