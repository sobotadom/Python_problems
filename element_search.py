from types import *
"""
Takes an ordered list of numbers and another number.
The function decides whether or not the given number is inside the list and returns( then print) an appopriate boolean
Use Binary Search

"""
__author__ = 'Dom'

def linear_search(order_list, a):
    is_there = False
    for i in range(0,len(order_list)):
        if order_list[i] == a:
            is_there = True

    return is_there

def binary_search(order_list, a):
    is_there = False
    midindex = ''
    first = 0
    last = len(order_list) - 1

    while not is_there and first <= last:
        mid = int((first + last)/ 2)
        if order_list[mid] == a:
            is_there = True
        else:
            if a < order_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return is_there


not_ordered = True
while not_ordered:

    listed = [int(x) for x in input('Input an ascending sequence of numbers\n').split()]
    if listed == sorted(listed):
        print('Is ordered')
        not_ordered = False
    else:
        print('Try again')

a = int(input('Enter the element to search for\n'))
print('Linear search result: ', linear_search(listed, a))
print('Binary search result: ', binary_search(listed, a))