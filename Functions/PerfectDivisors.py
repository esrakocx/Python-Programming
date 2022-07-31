print("Perfect Divisors\n")

def find_divisors(number):
    perfect_divisors = []

    for i in range(2, number):
        if number % i == 0:
            perfect_divisors.append(i)
    return perfect_divisors

while True:

    number = input("Number: ")

    if number == "q":
        print("Program is terminated...")
        break
    else:
        number = int(number)
        print("Perfect divisors are: ", find_divisors(number))

