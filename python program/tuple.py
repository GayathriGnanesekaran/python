a=(1,2,22.3,True,'gayuma')
print(a)
print(type(a))
#change is not possible in tuple
#slicing
print(a[1:3])
print(a[2:])
print(a[:3])
print(a[-2:])
print(a[:-1])
print(a[::-1])
#change is possible using type casting
a=(1,22,3,4,5)
print(a)
print(type(a))
b=list(a)
b.append(7)
print(b)
print(type(b))
a=tuple(b)
print(a)
#tuple print using for loop
a=(1,2,34,5)
for i in a:
    print(i)
#to check particular value using if condition
a=('gayu',1,2,2.3)
if 'gayu' in a:
    print("found")
else:
    print("not found")
#to find len
print(len(a))
#how python recognize value
a=(1)
print(type(a))
b=(1,)
print(type(b))
del(a)
#print(a)#name error
#concatenation
a=(1,2,3,4)
b=(3,4,5,6)
c=a+b
print(c)
print(c.count(3))
#nested tuple
c=(a,b)
print(c)
print(c[0])
print(c[1])
#multiple time print
x=('gayu',)*2
print(x)
a=(1,2,3,4,5)
print(min(a))
print(max(a))
