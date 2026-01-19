import random
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!@#$%^&*()_+-=[]{}|;:',.<>?/"
numbers = "0123456789"
input("Welcome to the Password Generator!\n")
l = int(input('How many letters would you like in your password? \n'))
s = int(input('How many symbols would you like in your password? \n'))
n = int(input('How many numbers would you like in your password? \n'))
password = ""
for i in range(l):
    password +=random.choice(letters)
for i in range(s):
    password +=random.choice(symbols)
for i in range(n):
    password +=random.choice(numbers)
password = list(password)
random.shuffle(password)
print(password)
print("".join(password))

a= list('sohail')
print(a)
