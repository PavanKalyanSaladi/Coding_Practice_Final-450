'''
List -  A list is a data structure that holds an ordered collection of items.
List starts and ends with [ ]
List elements doesn't need to have same type
List of lists are allowed - ['spam', 1.0, [10, 20]]
List indexing starts with 0 to N-1      N = Number of elements
'''

# Cretation of list
integers = [1, 2, 3, 4]
print(integers)

shoppingList = ['Milk', 'Cheese', 'Banana']
print(shoppingList)

mixedList = [2.4, 'spam', 99]
print(mixedList)

nestedList = [1, 2, 'spam', 'me', [1, 1.0, '1']]
print(nestedList)

empty = []          # empty list prints - []
print(empty)


# Acessing / Traversing a List
print(shoppingList[1])
print(shoppingList[-1])                 # -1 indexing starts from back -> -3 -2 -1
print('Bread' in shoppingList)

for item in mixedList:                  # Iterate through list
    print(item, end="_")
print()
for i in range(len(nestedList)):        # Iterate using index of list
    print(nestedList[i], end=" ")
print()
print([item for item in integers])      # Single line iteration