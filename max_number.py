num = input("Enter list of number seperated by commas")
num_split = num.split(',')
count = 0
number_list = []
for i in num_split:
    count += 1
for n in range(count):
    num_split[n] = float(num_split[n])
    number_list.append(num_split[n])
print(number_list)
for i in number_list:
    if number_list[0] < i:
        number_list[0] = i
print(f'Maximum number is {number_list[0]}')