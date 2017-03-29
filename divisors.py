__author__ = 'Dom'
#find all the divisors for a number



def divisorFinder(num):

    for i in range(1, num + 1):
        if(num % i == 0):
            print(i)
    return ;

num = int(input('Input the number to find divisors for\n'))
divisorFinder(num)