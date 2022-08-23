# Pairs of numbers denoting the sides of a rectangle

sides = [(3, 4), (10, 3), (5, 6), (1, 9)]

# area(x, y) function represents the area of any rectangular


def area(sides):
    return sides[0] * sides[1]


print(list(map(area, sides)))
