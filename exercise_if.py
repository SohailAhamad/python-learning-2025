your_name = input("Enter your name: ")
partner_name = input("Enter your partner's name: ")
your_name_lower = your_name.lower()
partner_name_lower = partner_name.lower()
a = your_name_lower.count('t')+partner_name_lower.count('t')+your_name_lower.count('r')+partner_name_lower.count('r')+your_name_lower.count('u')+partner_name_lower.count('u')+your_name_lower.count('e')+partner_name_lower.count('e')
b = your_name_lower.count('l')+partner_name_lower.count('l')+your_name_lower.count('o')+partner_name_lower.count('o')+your_name_lower.count('v')+partner_name_lower.count('v')+your_name_lower.count('e')+partner_name_lower.count('e')
percentage = str(a)+str(b)
if percentage < '10':
    print(f'Your score is {percentage}%, you go together like coke and mentos.')
elif percentage > '90':
    print(f'Your score is {percentage}%, you go together like peanut butter and jelly.')
else:
    print(f'Your score is {percentage}%, you go together like oil and water.')