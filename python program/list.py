
a=[1,22,33,4,5]
print(a)
print(type(a))
a[0]=100
print(a)
#slicing
print(a[0:3])
print(a[1:4])
print(a[1:])
print(a[:3])
print(a[:-1])
print(a[-3:])
print(a[::-1])
#mixed values
b=[1,True,'gayuma',12.3]
print(b)
print(b[0],"type is",type(b[0]))
print(b[1],"type is",type(b[1]))
print(b[2],"type is",type(b[2]))
print(b[3],"type is",type(b[3]))
#nested list
a=[1,True,'gayuma',[1,2,3,44]]
print(a)
print(type(a))
print(a[3][1])
#clear function
z=[1,2,3,4,5]
print(z)
z.clear()
print(z)
#copy fun
x=[4,5,6,7,8]
print(x)
y=x.copy()
print(y)
#count fun
a=[1,23,4,23,45,6]
print(a.count(23))
print(a.index(4))
print(len(a))
print(max(a))
print(min(a))
#pop fun it use index
a=[1,2,3,4,5]
a.pop(1)
print(a)
#remove fun using value
u=[1,22,4,5,6,7]
print(u.remove(1))
#append ffun
names=['gayuma','xxx']
names.append('yyyy')
names.append('little')
print(names)
#extend fun
name1=['iiiii','oooo']
names.extend(name1)
print(names)
#insert fun
names.insert(0,'ttt')
print(names)
#list constructor
print(list(range(5)))
print(list("gayu"))
#sort function
a=[2,3,51,25,7,8]
a.sort()
print(a)
a.sort(reverse=True)
print(a)
names=['orange','turteles','apple']
names.sort(reverse=True)
print(names)
names.sort(key=len)
print(names)


