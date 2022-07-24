print("Finding the hypotenuse of a right triangle\n")

a = int(input("Please enter the one of the perpendicular sides: "))
b = int(input("Please enter the other perpendicular side: "))

c = (a ** 2 + b ** 2) ** 0.5

print("Hypotenuse of the the right triangle is: {}".format(c))
