#name error
try:
    print(a)
except NameError:
    print("a is not defined")
    
#ZeroDivisionError
try:
    a=10/0
    print(a)
except ZeroDivisionError:
    print("denominator can't be zero")
    
#value error
try:
    a=int("gayu")
    print(a)
except ValueError:
    print("enter crt value")
#indexoutofbound
try:
    a=[1,2,3,4]
    print(a[10])
except IndexError:
    print("index out of bound")
#filenotfoundd
try:
    f=open("test.txt") 
except FileNotFoundError:
    print("fie not found")
else:
    print(f.read())
#multiple exception
try:
    a=10/0
    print(a)
    b=[1,2,3,44,5,6]
    print(b[10])
except ZeroDivisionError:
    print("den can't be zero")
except IndexError:
    print("index out of bound")
    
    
    
    
    
    
    
