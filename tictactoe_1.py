#Draw a gameboard
import sys
__author__ = 'Dom'

size = int(input('Please enter the size of the game board'))
rows = (2 * size) + 2
for i in range(1, rows):
    #odd rows  ...
    if i % 2 != 0:
        for j in range(1, size + 1):
            if j == size:
                sys.stdout.write('  __  \n')
            else:
                sys.stdout.write('  __  ')
    #even rows uses |
    else:
        for j in range(1, size + 1):
            if j == (size):
                sys.stdout.write('|    |\n')
            else:
                sys.stdout.write('|    |')


