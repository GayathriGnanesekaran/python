#instance variable-it is defined inside the constructor
class phone:
    def __init__(self,price,charger):
        self.price=price
        self.charger=charger
    def display(self):
        print(self.price)
        print(self.charger)
samsung=phone("6000","ctype")
samsung.display()
#class variable-it is used for fix the variable value
class phone:
    chargertype="ctype"#class variable
    def __init__(self,price):
        self.price=price
        
    def display(self):
        print(self.price)

        
samsung=phone("6000")
samsung.display()

    
