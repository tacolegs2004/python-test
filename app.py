# tuples

names = ("roger", 'adam', "james")

print("roger" in names)
print(type(names))
print(len(names))


#dictionaries

dog = {"name": "jack", "age": 6}
dog["favorite food"] = "meat"
del dog["age"]
print(dog.keys())
print(dog.get("name"))
print(list(dog.items()))
print(dog.popitem())
print(dog)



# sets

set1 = {"wanda", "cosmo"}
set2 = {"wanda", "rick"}

setds = set1 & set2

print(setds)



