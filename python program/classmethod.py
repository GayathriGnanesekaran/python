class laptop:
    chargertype="ctype"#class variable
    def __init__(self):#instance variable-it is defined using self
        self.brand="hp"
        self.price="12200"
        
    def setprice(self,price):
        self.price=price
    def getprice(self):
        print(self.price)
    @classmethod
    def changedchargertype(cls):
        cls.chargertype="btype"
        print("changed")
    @staticmethod
    def info():
        print("welcome")
hp=laptop()
hp.setprice=123000
hp.getprice()
hp.changedchargertype()#if you dont define class method,then we have to mention the cls inside the bracket
hp.info()
        
