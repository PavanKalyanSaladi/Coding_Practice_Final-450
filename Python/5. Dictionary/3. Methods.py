# Dictionary Methods
myDict = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}

dict1 = myDict.copy()
print(dict1)

myDict.clear()
print(myDict)

newDict = {}.fromkeys([1, 2 , 3], 0)
print(newDict)

print(dict1.get('name', 'Pavan'))       # key, value - value is optional. if key not found, it returns the value

print(dict1.items())

print(dict1.keys())

print(dict1.values())

dict1.popitem()
print(dict1)

print(dict1.setdefault('age', 30))      # same as get, also it adds the key if it doesn't exist
print(dict1.setdefault('sage', 30))
print(dict1)

print(dict1.pop('sage', 100))            # pop the key, if not found return value
print(dict1)

dict1.update({'test': 'value'})         # update/extend the dictionary with given key:value
print(dict1)