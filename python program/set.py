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
print("-------------------------------------------------------------------")
#join-it combines two sets using join()
a={1,2,3,4,5}
b={'a','g','h'}
c=a.join(b)
print(c)
