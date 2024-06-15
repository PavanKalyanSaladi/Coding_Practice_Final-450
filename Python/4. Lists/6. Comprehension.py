# List Comprehension of values
prev_list = [1, 2, 3]
print(prev_list, end=" -> ")
new_list = [new_item * 3 for new_item in prev_list]
print(new_list)

language = 'Python'
print(language, end=" -> ")
new_list = [letter for letter in language]
print(new_list)


# Conditional List Comprehension
prev_list = [-1, 10, -20, 2, -90, 60, 45, 20]
print(prev_list, end=" -> ")
new_list = [number for number in prev_list if number > 0]
print(new_list)

prev_list = [-1, 10, -20, 2, -90, 60, 45, 20]
print(prev_list, end=" -> ")
new_list = [number * number for number in prev_list if number < 0]
print(new_list)

sentence = 'My name is Elshad'
print(sentence, end=" -> ")
def is_consonant(letter):
    return letter.isalpha() and letter.lower() not in 'aeiou'
consonants = [letter if is_consonant(letter) else '' for letter in sentence]
print(consonants)