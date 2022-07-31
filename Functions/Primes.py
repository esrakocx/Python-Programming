print("~Primes~\n")


def prime(number):
    if number == 0:
        return False
    elif number == 1:
        return False
    elif number == 2:
        return True
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True

while True:
    number = input("Number is: ")

    if number == "q":
        break
    else:
        number = int(number)

        if prime(number):
            print(number, "is a prime number.")
        else:
            print(number, "is not a prime number.")
