__author__ = 'Dom'
"""
Write a program (using functions!) that asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order.
"""

string = str(input('Put in a sentence\n'))
list = string.split(' ')[::-1]
str = ' '.join(list)
print(str)
