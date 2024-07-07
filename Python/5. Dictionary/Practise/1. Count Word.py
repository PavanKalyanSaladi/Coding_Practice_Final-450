'''
Count Word Frequency
Define a function to count the frequency of words in a given list of words.

Example:

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
count_word_frequency(words) 
Output:

 {'apple': 3, 'orange': 2, 'banana': 1}
'''

def count_word_frequency(words):
    # TODO
    word_freq = dict()
    for word in words:
        if word in word_freq.keys():
            word_freq[word] += 1;
        else:
            word_freq[word] = 1
    return word_freq

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
print(count_word_frequency(words))