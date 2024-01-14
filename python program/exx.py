class shape:
    def area(self):
        return 0;
class rectangle:
    def area(self):
        l=10
        b=20
        print(l*b)
r1=rectangle()
r1.area()
'''
#2
class person:
    def __init__(self,name):
        self.name="name"
class student(person):
    def __init__(self,grade):
        super().__init__()
        self.grade="grade"
    def display(self):
        print(self.name,self.grade)
    
s1=student("a","p")
s1.display()
'''
#3
class vehicle:
    def start(self):
        print("vehicle started")
class car(vehicle):
    def start(self):
        print("car started")
        
        
