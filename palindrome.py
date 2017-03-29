__author__ = 'Dom'
"""
Ask the user for a string and print out whether this string is a palindrome or not.
"""


word = str(input('Please enter a word to check for palindromes'))
reverse = word[::-1]

if(word == reverse):
    print('Is Palindrome')
else:
    print('Not Palindrome')