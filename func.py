# functions




def name(name):
    print(f"hello {name}")
    return name, "syd", 7

print(name("taco"))

age = 8

def test():
    print(age)

print(age)
test()




def talk(phrase):
    def say(word):
        print(word)

    words = phrase.split(" ")
    for word in words:
        say(word)



talk("I am going home")





def count():
    count = 0

    def inc():
        nonlocal count
        count += 1
        print(count)

    inc()

count()









