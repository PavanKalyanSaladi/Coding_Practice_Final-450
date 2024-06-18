'''
Print the pairs, where their sum equals to a target number.

Input:-
[2, 7, 11, 9, 1]    9

Output:-
[0, 1]  -> 2 + 7 = 9
'''

def pairs(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                continue
            elif arr[i] + arr[j] == target:
                print(i, j)

n = int(input("Enter n value: "))
arr = []
for i in range(n):
    arr.append(int(input()))
pair_sum = int(input("Enter the sum of pairs: "))
pairs(arr, pair_sum)