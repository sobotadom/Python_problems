"""
Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.
"""
__author__ = 'Dom'

with open('one.txt','r') as prime:
   prime_list = [int(line.split()[0]) for line in prime]
with open('two.txt','r') as happy:
   happy_list = [int(line.split()[0]) for line in happy]

print('Common elements\n', list(set(prime_list) & set(happy_list)))