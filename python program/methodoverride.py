class animal():
    def sound(self):
        print("animal makes a sound")
class dog(animal):
    def sound(self):
        print("dog bark")
class bird(animal):
    def sound(self):
        print("bird song")
b1=bird()
b1.sound()
