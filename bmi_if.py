weight = float(input('Enter your weight:'))
height=float(input('Enter your height in mts:'))
bmi = round(weight / height ** 2,1)
Weight_to_Lose = round(weight - height ** 2 * 25, 1)
if bmi < 18.5:
    print(f'Your bmi is {bmi}, You are underweight')
elif bmi < 24.9:
    print(f'Your bmi is {bmi}, You are normal weight')
elif bmi < 29.9:
    print(f"Your bmi is {bmi},You are Overweight ,You need to lose {Weight_to_Lose} kg to reach a healthy weight.")
elif bmi < 34.9:
    print(f"Your bmi is {bmi},You are Obese ,You need to lose {Weight_to_Lose} kg to reach a healthy weight.")
else:
    print('Meet a doctor soon')

print('Wish you good health!')