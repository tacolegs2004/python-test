dogs = ["zaggy", "jock", "brian"]
dogs[2] = "taco"
dogs.insert(3, "ben")
dogs.append("john")
dogs += ["tammy", "jim"]

print("taco" in dogs)
print(dogs.index("ben"))
print(sorted(dogs, key=str.lower))
print(len(dogs))
