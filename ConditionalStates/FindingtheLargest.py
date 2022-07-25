print("~Find the largest number among the three numbers~\n")

number1 = float(input("Number 1: "))
number2 = float(input("Number 2: "))
number3 = float(input("Number 3: "))

if number1 >= number2 and number1 >= number3:
    print("{} is the biggest one!".format(number1))
    if number1 == number2 == number3:
        print("All the numbers are equal!")
    elif number1 == number2:
        print("{} and {} are equal.".format(number1, number2))
    elif number2 == number3:
        print("{} and {} are equal.".format(number2, number3))
    elif number1 == number3:
        print("{} and {} are equal.".format(number1, number3))
elif number2 >= number1 and number2 >= number3:
    print("{} is the biggest one!".format(number2))
    if number1 == number2 == number3:
        print("All the numbers are equal!")
    elif number1 == number2:
        print("{} and {} are equal.".format(number1, number2))
    elif number2 == number3:
        print("{} and {} are equal.".format(number2, number3))
    elif number1 == number3:
        print("{} and {} are equal.".format(number1, number3))
elif number3 >= number1 and number3 >= number2:
    print("{} is the biggest one!".format(number3))
    if number1 == number2 == number3:
        print("All the numbers are equal!")
    elif number1 == number2:
        print("{} and {} are equal.".format(number1, number2))
    elif number2 == number3:
        print("{} and {} are equal.".format(number2, number3))
    elif number1 == number3:
        print("{} and {} are equal.".format(number1, number3))
