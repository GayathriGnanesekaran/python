class student:
    def __init__(self):
        self.name="gayuma"
        self.regno="7"
    def display(self):
         print(self.name)
         print(self.regno)
s1=student()
print(s1.name)
print(s1.regno)
print(s1.display())
#pass the variable through object
class fruit:
    def __init__(self,col):
        self.colour=col
apple=fruit("red")
print(apple.colour)
#ex3
class teacher:
    def __init__(self,name,regnos):
        self.name=name
        self.regno=regnos
    def display(self):
        print(self.name)
        print(self.regno)
t1=teacher("gayu","12")
t2=teacher("gayuma","19")
t1.display()
t2.display()
#ex4
class calculator:
    def __init__(self,a,b):
        self.n1=a
        self.n2=b
    def add(self):
        print(self.n1+self.n2)
ob1=calculator(1,2)
ob1.add()
        
        
        

    
           
