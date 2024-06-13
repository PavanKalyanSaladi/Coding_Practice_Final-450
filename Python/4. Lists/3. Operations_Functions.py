# List Operations / Functions
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b               # + operator - concatenate lists 
print(c)

a = [0]
a = a * 4               # * operator - multiples the given thing
print(a)

print(len(c))           # len() - returns the count of ele's in list

print(max(c))           # max() - returns the highest value in list

print(min(c))           # min() - returns the highest value in list

print(sum(c))           # sum() - returns the sum of all items in list

print(sum(b)/len(b))    # / operator - returns the boolean division

print(sum(b)//len(b))   # // operator - returns the integer division


'''
List methods for insertion:-
 - insert()
 - append()
 - extend()
List methods for deletion():-
 - pop()
 - delete()
 - remove()
'''
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