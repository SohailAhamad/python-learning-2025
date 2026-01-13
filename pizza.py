size = input('Enter size of pizza (small/medium/large):')
price = 0
if size == 'small':
    price = 100
elif size == 'medium':
    price = 150
else:
    price = 200
pepperoni = input('Do you want pepperoni? (yes/no):')
if pepperoni == 'yes' and size == 'small':
    price += 30
elif pepperoni == 'yes' and (size == 'medium' or size == 'large'):
    price += 50
cheese = input('Do you want extra cheese? (yes/no): ')
if cheese == 'yes':
    price +=20
print(f'Your final bill is Rs.{price}')