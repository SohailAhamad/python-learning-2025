secret_password = 'codegreen123'
password=input('Enter your secret password')
while password != secret_password:
    print('Password incorrect,Try again!')
    password=input('Enter your secret password')
else:
    print('Access Granted!')