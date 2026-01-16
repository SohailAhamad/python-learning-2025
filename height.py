height = input("Enter heights separated by commas: ")
height_list = (height.split(','))
print(height_list)
count = 0
for i in height_list:
    count += 1
for n in range(0, count):
    height_list[n] = int(height_list[n])
    print(height_list[n])
sum_height = sum(height_list)
average_height = sum_height / count
   # print(height_list[n])
print("Sum of heights:", sum_height)
print("Average height:", round(average_height))

