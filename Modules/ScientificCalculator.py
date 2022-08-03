import math
import time

print("""
Please chose the operation: 

1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Value of Sin
6. Value of Cos
7. Value of Tan
8. Value of Log
9. Factorial
10.SquareRoot
11.Exponentiation
12.Exit

""")

while True:
    choice = input("Please enter your choice: ")

    if choice == "1":
        number1 = float(input("Number 1: "))
        number2 = float(input("Number 2: "))
        print("{} + {} = {}".format(number1, number2, number1 + number2))

    elif choice == "2":
        number1 = float(input("Number 1: "))
        number2 = float(input("Number 2: "))
        print("{} - {} = {}".format(number1, number2, number1 - number2))

    elif choice == "3":
        number1 = float(input("Number 1: "))
        number2 = float(input("Number 2: "))
        print("{} x {} = {}".format(number1, number2, number1 * number2))

    elif choice == "4":
        number1 = float(input("Number 1: "))
        number2 = float(input("Number 2: "))
        print("{} / {} = {}".format(number1, number2, number1 / number2))

    elif choice == "5":
        value = float(input("Value: "))
        print("sin({}) = {}".format(value, math.sin(value)))

    elif choice == "6":
        value = float(input("Value: "))
        print("cos({}) = {}".format(value, math.cos(value)))

    elif choice == "7":
        value = float(input("Value: "))
        print("tan({}) = {}".format(value, math.tan(value)))

    elif choice == "8":
        value = float(input("Value: "))
        print("log({}) = {}".format(value, math.log10(value)))

    elif choice == "9":
        value = int(input("Value: "))
        print("{}! = {}".format(value, math.factorial(value)))

    elif choice == "10":
        value = float(input("Value: "))
        print("√{}¯ = {}".format(value, math.sqrt(value)))

    elif choice == "10":
        value = float(input("Value: "))
        print("√{}¯ = {}".format(value, math.sqrt(value)))

    elif choice == "11":
        base = float(input("Base: "))
        exponent = float(input("Exponent: "))
        print("{} ^ {} = {}".format(base, exponent, math.pow(base, exponent)))

    elif choice == "12":
        print("Exiting....")
        time.sleep(1)
        break

    else:
        print("Incorrect input!")
        break
