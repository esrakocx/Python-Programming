print("~Greatest Common Divisor~\n")

def find_gcd(number1, number2):

    divisors = []

    for i in range(1, max(number1, number2)):
        if number1 % i == 0 and number2 % i == 0:
            divisors.append(i)

    return max(divisors)


while True:

    number1 = int(input("Number 1: "))
    number2 = int(input("Number 2: "))

    print("GCD:", find_gcd(number1, number2))
