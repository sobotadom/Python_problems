__author__ = 'Dom'

file = open('temp.txt', 'r+')
print(file.tell())
print(file.readline())
print(file.tell())
print(file.readline())
print(file.tell())
file.write('\nHELLO');

