a=list(range(5))
print(a)
print(list(range(1,5)))
#even
print(list(range(0,20,2)))
#odd
print(list(range(1,20,2)))
#to do the same work for several times
for i in range(5):
  x=int(input("enter the a"))
  y=int(input("enter the b"))
  c=x+y
  print("total is",c)
