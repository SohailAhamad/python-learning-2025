name = 'Bob'
age = 3000
print('Enter your Name')
input_name = input().strip()
print('Enter your age')
age_input = input().strip()
age = int(age_input)
if input_name == 'Bob':
    print('Hi Bob')
elif age < 12:
    print('You are not '+ name ,'Kiddo.')
elif age > 100 and age < 2000 :
    print('You are not '+ name ,'Grannie.')
elif age > 2000:
    print('Unlike you, ' + name +' is not an undead,immortal vampire')
