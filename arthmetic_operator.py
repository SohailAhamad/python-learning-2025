weight = input('Enter your weight in Kgs: ')
height = input('Enter your height in feet: ')
height = float(height) * 0.3048  # converting feet to meters
weight = float(weight)  # converting weight to float
bmi = weight // (height ** 2)
print('Your BMI is:', bmi)