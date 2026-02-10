import random as r
attempts = 0
num = r.randint(0,10)
selection = None
while selection != num:
    selection = int(input('Guess a number between 1 to 10'))
    attempts+=1

    if selection > num :
        print('Number you guessed is higher, pick another number')
    elif selection < num :
        print('Number you guessed is lower, pick another number')
    
print(f'You guessed the number correct in {attempts} attempts')
        