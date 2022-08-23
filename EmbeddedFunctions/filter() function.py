sides = [(3, 4, 5), (6, 8, 10), (3, 10, 7), (8, 17, 15), (7, 9, 2)]

def triangle(sides):
    if abs(sides[1] - sides[2]) < sides[0] < sides[1] + sides[2]:
        return True
    elif abs(sides[0] - sides[2]) < sides[1] < sides[0] + sides[2]:
        return True
    elif abs(sides[0] - sides[1]) < sides[2] < sides[0] + sides[1]:
        return True
    else:
        return False


print(list(filter(triangle, sides)))
