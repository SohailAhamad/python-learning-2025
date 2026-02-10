height = int(input("Enter your height in feet: "))
bill = 0
if height > 3:
    print('You can ride!')
    age = int(input("Enter your age: "))   
    if age < 12:
        bill = 150
        print('Ticket price is Rs.150')
    elif age < 18:
        bill = 200
        print('Ticket price is Rs.200')
    else:
        bill = 250
        print('Ticket price is Rs.250')
    photo = input("Do you want a photo? (yes/no): ")
    if photo == "yes":
        bill += 100
    print(f'Your final bill is Rs.{bill}')
else:
    print('You cannot ride!')