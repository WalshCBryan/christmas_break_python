from array import *
array_num = array('i', [1,3,5,7,9])
for i in array_num:
    print(i)
print("Access first three items individually")
print(array_num[0])
print(array_num[1])
print(array_num[2])

array_num.append(11)
print(array_num)
print("Length in bytes of one array item: "+str(array_num.itemsize))


array_num.append(11)
print("Number of occurrences of the number 3 in the said array: "+str(array_num.count(11)))

