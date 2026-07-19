#inheritance is like a family tree , a child class (subclass) inherits traits from is parents class (superclass)

class Animal:  # Parent class (superclass)
    location = "india"
    def __init__(self, name): #called cunstructor
        self.name = name
 
    def speak(self):
        print("Generic animal sound")

class Dog(Animal):
    def speak(self):
        super().speak() #super is used to call the parent class methods
        print("Woof!")

a = Dog("Bruno")
a.speak()        
# print(a.location)