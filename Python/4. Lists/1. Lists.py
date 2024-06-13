'''
List -  A list is a data structure that holds an ordered collection of items.
List starts and ends with [ ]
List elements doesn't need to have same type
List of lists are allowed - ['spam', 1.0, [10, 20]]
List indexing starts with 0 to N-1      N = Number of elements
List methods for insertion:-
 - insert()
 - append()
 - extend()
List methods for deletion():-
 - pop()
 - delete()
 - remove()
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



# Update / Insert into list
myList = [1, 2, 3, 4, 5, 6, 7]
print(myList)
myList[2] = 33
myList[4] = 55
print(myList)

myList.insert(0, 11)
print(myList)
myList.append(10)
print(myList)
myList.extend([11, 12, 13])
print(myList)



# Slice / Delete from list
myList = ['a', 'b', 'c', 'd', 'e', 'f']
print(myList[0:2])                          # prints 0 to 2 index values, excluding 2
print(myList[:2])                           # prints 0 to 2 index values, excluding 2
print(myList[1:])                           # prints 1 to n-1, n is number of elements
print(myList[:])                            # prints entire list
print(myList[-1:])                          # prints -1 index element
myList.pop()                                # pops last element, you can pass index as well
print(myList)
del myList[1]                               # deletes the element of given index
print(myList)
del myList[4:]                              # deletes the element from 4 to N-1
print(myList)
myList.remove('e')                          # Removes the given value if exists
print(myList)