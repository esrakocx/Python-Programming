class Squares():
    def __init__(self, max = 0):
        self.max = max
        self.power = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.power <= self.max:
            result = self.power ** 2
            self.power += 1
            return result
        else:
            self.power = 1
            raise StopIteration


square = Squares(5)
iterator = iter(square)
'''
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
'''
for i in square:
    print(i)
for j in square:
    print(j)