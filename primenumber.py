__author__ = 'Dom'
"""
Ask the user for a number and determine whether the number is prime or not
"""


num = int(input('Enter a number to check for primeness\n'))
count = 0

for i in range(2, num):
    if((num % i) ==0):
        count+=1
if(count == 0):
    print('Is Prime')
else:
    print('Is not Prime')