import random
random_number = random.randint(0,3)
Rock = 0
Paper = 1
Scissors = 2

a = input('Enter your choice (Rock,Paper,Scissors):')
if random_number == 0 and a == 'Rock':
    print("It's a tie!")
elif random_number == 0 and a == 'Paper':
    print("You win!")
elif random_number == 0 and a == 'Scissor':
    print("You Lose")
elif random_number == 1 and a == 'Scissors':
    print("You win!")
elif random_number == 1 and a == 'Paper':
    print("It's a tie!")
elif random_number == 1 and a == 'Rock':
    print("You Lose")
elif random_number == 2 and a == 'Scissors':
    print("It's a tie!")
elif random_number == 2 and a == 'Paper':
    print("You Lose")
elif random_number == 2 and a == 'Rock':
    print("You win!")
print(random_number)