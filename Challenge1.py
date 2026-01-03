try:
    age = int(input("Enter your age"))
except ValueError:
    print("Please enter a valid age.")
else:
    if age < 13 :
        print("You're a Kid!")
    elif age <  18 :
        print("You're a teenager!")
    elif age < 65 :
        print("You're an adult!")
    else:
        print("You're a senior!")




    
