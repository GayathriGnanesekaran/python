#super keyword-super().__init__() and it is used to call parent class constructor
class a():
    def __init__(self):
        print("a")
    def display(self):
        print("class a")
class b():
    def __init__(self):
        super().__init__()
        print("b")
    def display(self):
        print("class b")
class c(a,b):#left side call agum
    def __init__(self):
        super().__init__()
        print("c")
    def display(self):
        print("class c")
ob1=b()
ob1.display()
gayu=c()
gayu.display()
        
        
        
