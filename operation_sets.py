a = {1,4,5,7,3,6}
b = {2,5,6,7,6,0,1001}
#Union
print(a.union((3,5,6,7,99,20)))
print(a.union([88,98,8,100]))
print(a | b)
a.update(b)
print(a)
a.update([89,98,3,45,6])
print(a)
a |= b
print(a)
#Intersection
print(a.intersection((10,20,4,3)))
print(a & b)
a.intersection_update([5,6,7,8,100])
print(a)
#a.intersection_update({100,200,300,600})
print(a)
print(b)
a.difference(b)
print(a)