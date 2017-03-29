__author__ = 'Dom'
#prints out wheter the input is odd or even
num = int(input('Hey give me a number\n'))
check = int(input('Hey give me a second number'))

if(check % num == 0):
    print('The second number divides evenly into the first')
else:
    print('The second number does not divide into the first')