from functools import reduce

lambda num : num * 2

add = lambda a, b : a + b

print(add(2, 4))




numbers = [2, 4, 5, 3, 2, 6]

result = map(lambda a : a * 2, numbers)

print(list(result))


res = filter(lambda n : n % 2 == 0, numbers)

print(list(res))

expenses = [
    ("dinner", 80),
    ("bread", 12)
]

sum = reduce(lambda a, b: a[1] + b[1], expenses)

print(sum)
