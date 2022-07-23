"""
Finding the roots of a quadratic equation with one unknown

Equation is: ax^2 + bx + c

To find the delta: b ** 2 - 4 * a * c

First root: (-b - delta ** 0.5) / (2*a)
Second root: (-b + delta ** 0.5) / (2*a)

"""

print("~Equation Solving Program~")

print("Please enter your equation's a value: ")
a=int(input("a:"))
print("Please enter your equation's b value: ")
b=int(input("b:"))
print("Please enter your equation's c value: ")
c=int(input("c:"))

delta=b ** 2 - 4 * a * c

root1=(-b-delta**0.5)/(2*a)
root2=(-b+delta**0.5)/(2*a)

print("Your equation's first root: {}\nYour equation's second root: {}\n".format(root1,root2))