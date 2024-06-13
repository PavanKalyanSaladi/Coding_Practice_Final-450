# Strings to Lists
a = 'spam'
b = list(a)         # Iterates through 'a' and assign to list 'b'
print(b)

a = 'spam mail received'
b = a.split(' ')         # splits the string using ' ' delimiter
print(b)

a = [5, 1, 4, 2, 7, 6, 11]
a.sort()
print(a)