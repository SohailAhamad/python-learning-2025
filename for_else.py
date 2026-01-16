a = [1,55,43,87,44,32]
#b=[]
for i in a:
    #b.append(i)
    if i % 2 == 0:
       print(f'Found even number: {i}')
       break
else:
    print('No Even Number Found')
#print(b)