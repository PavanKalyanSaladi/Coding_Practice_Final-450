#Nested Loops

def print_items(n):
    for i in range(n):      # O(N)
        for j in range(n):      # O(N)
            print(i, j)

print_items(10)             # O(N * N) = O(N^2)


def print_items(n):
    for i in range(n):      # O(N)
        for j in range(n):      # O(N)
            for k in range(n):      # O(N)
                print(i, j, k)

print_items(10)             # O(N * N * N) = O(N^3)
# For Big O it doesn't matter if it 3 or 4 considered as O(N^2)