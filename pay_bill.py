import random
names = input('Enter your names seperated by commma')
name_list = names.split(',')
length = len(name_list)
random_index = random.randint(0,length-1)
print(f'{name_list[random_index]} is going to pay the bill')