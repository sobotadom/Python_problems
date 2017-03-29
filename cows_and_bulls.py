import random
__author__ = 'Dom'


if __name__=="__main__":
    generate =  str(random.randint(0,9999))
    guessnum = 0

    print("Let's play a game of Cowbull!")
    print("I will generate a number, and you have to guess the numbers one digit at a time.")
    print("For every number in the wrong place, you get a cow. For every one in the right place, you get a bull.")
    print("The game ends when you get 4 bulls!")
    print("Type exit at any prompt to exit.")
    print('generate', generate )
    while True:

        guessnum += 1
        num = input('Please enter a 4 digit number\n')
        cows = 0
        bulls = 0
        if num == 'exit':
            print('Good Bye')
            break
        elif len(num) != 4:
            print('Try Again')
        else:
            for i in range(0,4):
                if num[i] == generate[i]:
                    cows += 1
                else:
                    bulls += 1


            print('Cows: ', cows, '\nBulls: ', bulls)
            if cows == 4:
                print('You guessed the right number ', generate, ' in ', guessnum, ' guessed!' )
                break;