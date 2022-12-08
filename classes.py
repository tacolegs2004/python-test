# classes

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print("woof")



roger = Dog("roger", 15)

print(type(roger))

print(roger.name)
print(roger.age)
print(roger.bark())



















