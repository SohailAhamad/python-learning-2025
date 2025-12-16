def isPhooneNumber(text):
    if len(text) != 12:
        return False # not phone number-sized
    for i in range(0,3):
        if not text[i].isdecimal():
            return False # no area code
    if text[3] != '-':
        return False # missing dash
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False # missing dash
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

#print(isPhooneNumber('415-555-1234'))
    
#print('Enter your mobile number')
#PhoneNumber = input()

#if isPhooneNumber(PhoneNumber) == True:
 #   print('Here is your number' + PhoneNumber)
#else :
 #   print('Check your number')

message = 'Call me 411-422-9083 tomorrow or at 432-928-8727'
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhooneNumber(chunk):
        print('Phone Number Found : ' + chunk)
        foundNumber = True
if not foundNumber:
    print('Could not find any phone number')
    
