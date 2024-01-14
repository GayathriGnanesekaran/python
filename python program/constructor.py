#inbuilt function --init-- and it is used automaticcally
class laptop:
    def __init__(self):
        print("demo")
    def display(self):
        print("hhii")
hp=laptop()#here we dont call anything so it took init
#variable are craeted using constructor
class lap:
    def __init__(self):
        self.ram=""
        self.processor=""
hp=lap()
hp.ram="6gb"
hp.processor="i5"
print(hp.ram)
#SELF keyword  is used to denote current object
class laptops:
    def __init__(self):
        self.ram=""
        self.processor=""
    def display(self):
        print("ram is",self.ram)
        print("processor is",self.processor)
hp=laptops()
dell=laptops()
hp.ram="6gb"
hp.processor="i5"
dell.ram="8gb"
dell.processor="i7"
dell.display()
hp.display()

        
        
