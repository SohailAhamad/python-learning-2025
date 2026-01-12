try:
    age = int(input("Please enter your age: "))
except ValueError:
    print("Invalid input. Please enter a valid age.")
else:
    if age < 0:
        print("Age cannot be negative.")
    elif age < 13:
        print("You're a kid!")
    elif age < 18:
        print("You're a teenager!")
    elif age < 65:
        print("You're an adult!")
    else:
        print("You're a senior!")