__author__ = 'Dom'
"""
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
"""

print('Welcome to Rock, Paper, Scissors\nMake your Moves and see who wins\nInput exit to terminate')
first_record = []
second_record = []


def rps(first, second):
    if(first==second):
        first_record.append('Draw')
        second_record.append('Draw')
    elif((first=='Rock' and second=='Paper') or (first=='Paper' and second=='Scissors') or (first=='Scissors' and second=='Rock') ):
        first_record.append('Lose')
        second_record.append('Win')
        print('Player 2: ', second, ' beats Player 1: ', first)
    elif((first=='Rock' and second=='Scissors') or (first=='Paper' and second=='Rock') or (first=='Scissors' and second=='Paper')):
        second_record.append('Lose')
        first_record.append('Win')
        print('Player 1: ', first, ' beats Player 2: ', second)
    return ;



stop = 1
while stop==1:
    i = True
    j = True

    #first command input validation
    while(i):
        first = str(input('First Player move\n'))
        if(first == 'Rock'or first == 'Paper'or first == 'Scissors'):
            i = False
        elif first == 'Exit':
            i = False
            j = False
            stop = 0
        else:
            print('Try again')
    #second command input validation
    while(j):
        second = str(input('Second Player move\n'))
        if second == 'Rock' or second == 'Paper'or second == 'Scissors':
            j = False
        elif(second == 'Exit'):
            j = False
            stop = 0
        else:
            print('Try again')

    if(stop == 0):
        break;
    else:
        rps(first,second)

print('First Player Record ', first_record)
print('Second Player Record ', second_record)