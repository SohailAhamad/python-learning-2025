Weight = float(input("Enter your weight in kg: "))
Height = float(input("Enter your height in meters: "))
BMI = round(Weight / (Height ** 2), 1)
if BMI > 25:
    Healthy_weight = Height ** 2 * 25
    Weight_to_Lose = round(Weight - Healthy_weight, 1)
    print(f"You need to lose {Weight_to_Lose} kg to reach a healthy weight.")
else :
    print(f"You are already at a healthy weight. Your BMI is {BMI}.")
