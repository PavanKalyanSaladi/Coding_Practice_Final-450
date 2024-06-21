'''
What is Dictionary?
A dictionary is a collection of unordered, changeable and indexed.
It is defined as "key: value" pair in {}.

Ex:-
Miller: a person who owns or works in a corm mill

variable = dict(key=value)
variable = {key: value}
'''

# Dictionary Creation
my_dict = dict()
print(my_dict)

eng_sp = dict(one='uno', two='dos', three='tres')
print(eng_sp)

eng_sp2 = {'one':'uno', 'two':'dos', 'three':'tres'}
print(eng_sp2)

eng_sp_list = [('one', 'uno'), ('two', 'dos'), ('three', 'tres')]
eng_sp3 = dict(eng_sp_list)
print(eng_sp3)


# Insert / Update an element
my_dict = {'name': 'Pavan', 'age': 23}
#print(my_dict)
my_dict['age'] = 22
print(my_dict)
my_dict['address'] = 'Hyderabad'
print(my_dict)


# Traversing a dictionary
def traverseDict(my_dict):
    for key in my_dict:
        print(key, my_dict[key])

traverseDict(my_dict)