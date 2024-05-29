def print_items(n):
    for i in range(n):
        print(i)
print_items(10)

#Deletion of specific card -> It can be last card

def find_n(arr, n):
    for i in arr:
        if i == n:
            return "Found"
print(find_n([1, 2, 3, 4, 5], 5))