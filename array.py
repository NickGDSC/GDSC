a = [1,3,5,6,7,"Hello","World"]
print(type(a))
print (a)
b = a[:]
print(b)
c = list(b)
print(c)

a = list()
a.append("Nick without nick")
print(a)

a = [1,3,5,6,7,"Hello","World"]
a.remove(3) #по значению
del a[0] #по индексу
del a[-1] #по индексу с конца
a[2] = 755
print(a)
print(a[1:3]) #диапозон