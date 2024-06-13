# Searching for an element in the list

def searching(myList, target):
    if target in myList:
        print(f"{target} is in the list.")
    else:
        print(f"{target} is in not the list.")

myList = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target = 50
searching(myList, target)
searching(myList, 5000)


# Linear Search
def linear_search(l_list, l_target):
    for i, value in enumerate(l_list):          # i is index and value is target
        if value == l_target:                   # If target is found -
            return i                            #   - it returns the index
    return -1

print(linear_search(myList, target))