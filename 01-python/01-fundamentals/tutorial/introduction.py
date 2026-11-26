name = str("Osman")
point = int(98)
point_avg = float(95.6)
print(type(name))
print(type(point))
print(type(point_avg))
myList= []
name2 = name[2::]
point2 = point/10
point_avg2= point//10
myList.append(name2)
myList.append(point2)
myList.append(point_avg2)
print(myList)
myList.insert(len(myList) // 2, "aktif")
print(myList)
