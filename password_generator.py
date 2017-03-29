import random
__author__ = 'Dom'

population = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890_=+!@#$%^&*()-<>?{}|;'
response = ''
results = []
while response != 'N':
    response = str(input('Want a password? Options: Y / N'))

    if response == 'Y':
        temp = ''.join(random.sample(population, random.sample(range(8, 15), 1)[0]))
        results.append(temp)
        print(temp)

    elif response == 'N':
        print('No Password Generated')
    else:
        print('Try Again')

print('Passwords Generated\n', results)