import re

message = 'Call me 412-345-2345 tomorrow , or at 432-903-0998'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumRegex.findall(message))
