number1=input("Please enter the first number: ")
number2=input("Please enter the second number: ")

print("Values before being changed:\n1st number:{}\n2nd number:{}\n".format(number1, number2))
number1, number2 = number2, number1
print("Values after being changed:\n1st number:{}\n2nd number:{}".format(number1, number2))


