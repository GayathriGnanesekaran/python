#single inheritance
class dad():
    def phone(self):
        print("dad's phone")
class son(dad):
    def laptop(self):
        print("son's laptop")
ram=son()
ram.laptop()
ram.phone()
#multiple inheritance
class dad():
    def phone(self):
        print("dad's phone")
class mom():
     def sweet(self):
        print("sweety")
class son(dad,mom):
    def lap(self):
        print("sons phone")
gayu=son()
gayu.lap()
gayu.sweet()
gayu.phone()
#multilevel inheritance
class dad():
    def phone(self):
        print("dad's phone")
class mom(dad):
     def sweet(self):
         print("sweety")
class son(mom):
    def lap(self):
        print("sons phone")
nila=son()
nila.sweet()
nila.phone()
nila.lap()
#hierrachial inheritance
class dad():
    def phone(self):
        print("dad phone")
class son1(dad):
    pass
class son2(dad):
    pass
class son3(dad):
    pass
s1=son1()
s1.phone()
s2=son2()
s2.phone()
#hybrid
class dad():
    def phone(self):
        print("dad phone")
class land():
    def prop(self):
        print("haapppy")
class son1(dad,land):
    pass
class son2():
    pass
        
