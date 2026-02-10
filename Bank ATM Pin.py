secret_pin = "1234"
attempts = 3

while attempts > 0:
    user_input = input(f"Enter your PIN ({attempts} attempts left): ")
    
    if user_input == secret_pin:
        print("--------------------")
        print("Access Granted!")
        break
        # 1. ??? What goes here to skip the "Locked" message?
        
    else:
        attempts-=1
        # 2. ??? How do we decrease the attempts?
        print("Incorrect PIN.")

else:
    # This only runs if the loop finishes naturally (attempts hit 0)
    print("--------------------")
    print("ACCOUNT LOCKED.")