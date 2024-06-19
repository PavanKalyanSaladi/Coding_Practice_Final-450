'''
Duplicate Number
Write a function to remove the duplicate numbers on given integer array/list.

Example

remove_duplicates([1, 1, 2, 2, 3, 4, 5])
Output : [1, 2, 3, 4, 5]
'''

def remove_duplicates(arr):
    #TODO
    unique_list = []
    seen = set()
    for num in arr:
        if num not in seen:
            unique_list.append(num)
            seen.add(num)
    return unique_list

print(remove_duplicates([1, 1, 2, 2, 3, 4, 5]))