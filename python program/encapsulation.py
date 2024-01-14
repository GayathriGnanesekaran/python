class company():
    def __init__(self):
        self.__companyname="google"#private class-it is accessed with in the class
    def display(self):
         print(self.__companyname)
         
ca=company()
ca.display()
class com():
    def __init__(self):
        self._companyname="google"#private class-it is accessed with in the class
    def display(self):
         print(self._companyname)
class b(com):
    pass
         
ca=com()
ca.display()
b1=b()
b1.display()



         
