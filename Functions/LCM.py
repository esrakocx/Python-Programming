print("~Least common multiplier~\n")

def find_lcm(number1, number2):

    multipliers = []

    for i in range(1, number2+1):
        for j in range(1, number1+1):
            if number1 * i == number2 * j:
                multipliers.append(number1 * i)
    return min(multipliers)


while True:
    number1 = int(input("Number 1: "))
    number2 = int(input("Number 2: "))
    print("LCM ({},{}) = {}".format(number1, number2, find_lcm(number1, number2)))


