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