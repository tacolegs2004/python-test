# loops

condition = True

while condition == True:
    print("lol")
    condition = False

count = 0

while count < 10:
    print("the condition is true")
    count = count + 1



items = [2, 5, 7, 8]

for index, item in enumerate(items):
    if item < 3:
        continue
    print(index + 1, item)









