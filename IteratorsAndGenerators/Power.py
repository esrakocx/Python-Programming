class Power3():

    def __init__(self, max=0):
        self.max = max
        self.power = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.power <= self.max:
            result = 3 ** self.power
            self.power += 1
            return result
        else:
            raise StopIteration


power3 = Power3(6)
for i in power3:
    print(i)
