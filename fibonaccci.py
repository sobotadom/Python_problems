__author__ = 'Dom'
"""
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them
"""


def fibonacci(num):
	current = 1
	previous = 0
	fibo = []
	for i in range(1,num + 1):
		temp = current
		current += previous
		previous = temp
		fibo.append(previous)
	return(fibo);





num = int(input('How many fibonacci numbers do you want?'))
print(fibonacci(num))