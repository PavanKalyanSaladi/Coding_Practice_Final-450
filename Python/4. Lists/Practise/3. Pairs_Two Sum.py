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



'''
Pairs problem - 2
Write a function to find all pairs of an integer array whose sum is equal to a given number. Do not consider commutative pairs.

Example

pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
Output : ['2+5', '4+3', '3+4', '-2+9']


Note:

4+3 comes from second and third elements from the main list.

3+4 comes from third and seventh elements from the main list.
'''
def pair_sum_func(myList, sum):
    # TODO
    pairs = []
    for i in range(len(myList)):
        for j in range(i + 1, len(myList)):
            if myList[i] == myList[j]:
                continue
            if myList[i] + myList[j] == sum:
                pairs.append(str(myList[i]) + "+" + str(myList[j]))
    return pairs

n = int(input("Enter n value: "))
arr = []
for i in range(n):
    arr.append(int(input()))
pair_sum = int(input("Enter the sum of pairs: "))
print(pair_sum_func(arr, pair_sum))