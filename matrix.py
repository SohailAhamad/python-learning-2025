list1 = [1,1,1]
list2 = [0,1,0]
list3 = [1,0,1]
matrix = [list1,list2,list3]
print(f'{list1}\n{list2}\n{list3}')
position = input('Enter the position to change:')
row_selected = int(position[0])
column_selected = int(position[1])
row_position = matrix[row_selected-1]
row_position[column_selected-1] = 'X'
print(f'{list1}\n{list2}\n{list3}')