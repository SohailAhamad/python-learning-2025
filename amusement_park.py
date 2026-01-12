age = int(input('Enter your age :'))
if age <= 18:
    print('You are eligible for a child ticket.')
    height = int(input('Enter your height in ft:'))
    if height > 4 :
        print("You are allowed to ride.")
    elif height == 4:
        print('You can ride with an adult.')
    else:
        print('grow up kiddo')
else:
    print('Pay for an adult ticket.')