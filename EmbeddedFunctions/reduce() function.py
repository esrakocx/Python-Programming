from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filter = list(filter(lambda x : x % 2 == 0, numbers))

print(reduce(lambda x, y: x + y, filter))


