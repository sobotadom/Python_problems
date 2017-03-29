import random

__author__ = 'Dom'
"""
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""




results = []
num = random.sample(range(1,10), 1)

while True:

    mynum = input('Pick a Number between 1 and 9\n')
    if(mynum == 'Exit'):
        break;
    elif(int(mynum) > num[0]):
        print('Too high')
        results.append('High')
    elif(int(mynum) == num[0]):
        print('Matches')
        results.append('Match')
        break;
    elif(int(mynum) < num[0]):
        print('Too Low')
        results.append('Low')
    else:
        print('Try again')

print('Number ', num[0])
print('Number of guesses: ', len(results))
print('Results: ', results)