name={'yyyy','huii',2,3}
print(name)
print(type(name))
#access element for loop
for i in name:
    print(i)
#value cannot changed in set but we can add it
name.add(5)
print(name)
#update
a={1,8,9}
name.update(a)
print(name)
#remove function is used to delete the data and it give error when the mentioned not present
name.remove(2)
print(name)
#discard it does not provide error
name.discard(10)
print(name)
#pop use index
name.pop()
print(name)
#clear
name.clear()
print(name)
del name
#remove duplicate value
a={1,2,3,5,7,1,2,}
print(a)
#join-it combines two sets using join()
x={1,2,3,4,5}
y={1,2,4}
z=x.intersection(y)
print(z)
#intersected value store in x then we use update
x.intersection_update(y)
print(x)
x={1,2,3,4,5}
y={1,2,4}
z=x.union(y)
print(z)
#intersected value store in x then we use update
x.update(y)
print(x)
#symmetric differenece-it displays not equal value
a={1,2,3,4}
b={2,3,5,6}
c=a.symmetric_difference(b)
print(c)
a.symmetric_difference_update(b)
print(a)
#disjoint
t={3,4,5,6}
u={3,4,5,6}
o=t.isdisjoint(u)
print(o)
#subset
q={1,2,3,4,5}
w={1,2,3,4,5,6}
s=q.issubset(w)
print(s)
s=q.issuperset(w)
print(s)
print(o)
