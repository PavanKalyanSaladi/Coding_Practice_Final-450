#Drop Constants:

def print_items(n):
    for i in range(n):      # O(N)
        print(i)
    for j in range(n):      # O(N)
        print(j)

print_items(10)      # O(N + N) = O(2N) = O(N)


def print_items(n):
    for i in range(n):      # O(N)
        for j in range(n):      # O(N)
            print(i, j)
    
    for k in range(n):
        print(k)

print_items(10)            # O(N * N) + O(N) = O(N^2) + O(N) = O(N^2)