# This a guess the number game
import random

print('hello.What is your name?')
name = input()

print ('Well,' + name + ', I am thinking of a number between 1 to 10')
secretNumber = random.randint(1,10)

for guessesTaken in range(1,6) :
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')

    else:
        break

if guess == secretNumber:
    print('GoodJob,' + name + '! you guessed my number in '+str(guessesTaken) + ' guesses.')
else:
    print('Nope. The Number I was thinking of was ' + str(secretNumber))

        
