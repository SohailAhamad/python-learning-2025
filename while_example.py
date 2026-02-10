total = 0
num = int(input('Enter numbers to count(i>0), to stop enter 0'))
while num != 0:
     total = total+num
     num = int(input('Enter numbers to count(i>0), to stop enter 0'))
print(f'Total is {total}')