print("Enter your age")
age = int(input())
if age < 13 :
    print("You're a Kid!")
elif age <= 13 and age <  18 :
    print("You're a teenager!")
elif age <=18 and age < 65 :
    print("You're an adult!")
elif age >= 65 :
    print("You're a senior!")
else:
    print("Please enter a valid age.")
