print("Is it a perfect number?")

divisors = list()

number = int(input("Number: "))
i = 1
while i < number:
    if number % i == 0:
        divisors.append(i)
    i += 1
if sum(divisors) == number:
    print("{} is a perfect number!".format(number))
else:
    print("{} is not a perfect number!".format(number))

