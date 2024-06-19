'''
This program return whether the given two lists are permutation to each other.
True if both are permutation to each other, False if not.

The definition of a permutation is one possible ordered arrangement of some or 
    all objects in a set. For example, 
    given the set of numbers {1, 2, 3}, 
    the arrangements 123, 321, and 213 
    are three of the possible permutations of the set.

Example:- 
l1 = [1, 2, 3]  &   l2 = [3, 1, 2]
output:-
True
'''

def permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    return False

print(permutation([1, 2, 3], [3, 1, 2]))
print(permutation(['a', 'b', 'c'], ['b', 'c', 'a']))
print(permutation(['a', 'b', 'c'], ['b', 'd', 'a']))