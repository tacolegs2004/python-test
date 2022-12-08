# classes

class Pet:
    def walk(self):
        print('walking...')


class Dog(Pet):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print("woof")
        
class Cat(Pet):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        print("meow")



roger = Dog("roger", 15)
perry = Cat("perry", 4)
print(type(roger))
print(type(perry))
print(roger.name)
print(roger.age)
roger.bark()
roger.walk()
print(perry.name)
print(perry.age)
perry.meow()
perry.walk()


















