#function call itself
#define
def welcome():
    print("hiiiii")
    

#call    
welcome()
welcome()

#1.No return type and without arguments ex
def addition():
    a=int(input("enter a"))
    b=int(input("enter b"))
    c=a+b
    print(c)
addition()
#2.No return type with arguments
def subtraction(a,b):
    c=a-b
    print(c)
subtraction(23,4)
#3.return type and without arguments
def mul():
    a=int(input("enter the a:"))
    b=int(input("enter the b:"))
    c=a*b
    return c
print(mul())
#4.return type with arguments
def divide(a,b):
    c=a/b
    return c
print(divide(6,3))
#5.arbitary arguments function-we can pass lots of arguments and use*
def college(*students):
   print(students)
college('yyyy','uuu','uuuuu','pppp')
#6.keyword arguments
def message(name,age):
 print(name,age)
message(name="gayu",age=23)
message(age=23,name="gggg")
#7.arbitary keyword arguments
def data(**items):
  print(items)
data(name="gayu",age=34,gender="male",lot=1)
#8.default parameter function
def multiple(name,city="salem"):
    print(name,city)
multiple("gayu","covai")
multiple("oooo")
#9.passing a list as an arguments
def total(marks):
   return sum(marks)
print(total([1,2,3,4,5,6,7]))




    

