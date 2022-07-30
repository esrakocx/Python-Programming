print(""" 
***********************
~Calculator~

Operations:

+ -> Addition
- -> Subtraction
x -> Multiplication
/ -> Division

***********************
""")

number1 = float(input("Please enter the first number you want to operate: "))
number2 = float(input("Please enter the second number you want to operate: "))
operation = input("Please enter the operation you want to do:")

if operation == "+":
    print("{} + {} = {}".format(number1, number2, number1+number2))
elif operation == "-":
    print("{} - {} = {}".format(number1, number2, number1-number2))
elif operation == "x":
    print("{} x {} = {}".format(number1, number2, number1*number2))
elif operation == "/":
    print("{} / {} = {}".format(number1, number2, number1/number2))
else:
    print("You entered wrong operation, please try again!")
