import sys
__author__ = 'Dominik Sobota'
"""
Write a program that takes a list of numbers (for example,
a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list.

I will use terminal arguments to make a list
"""
list = ''

if len(sys.argv) < 2:
    print("Arguments incorrect, default list created")
    list = [1,13,14,22,35,76,8,97]
else:
    list = sys.argv[1:]

print('Your inputted list: ', list)

print('The ends of your list: ',[list[0],list[-1]])
