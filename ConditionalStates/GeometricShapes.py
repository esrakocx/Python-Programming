print("Geometric Shapes Calculator\n")

print("Enter 1 to find the type of quadrilateral\nEnter 2 to find the type of triangle\n")
choice = input("Choice: ")

if choice == "1":
    a = int(input("Enter first edge: "))
    b = int(input("Enter second edge: "))
    c = int(input("Enter third edge: "))
    d = int(input("Enter fourth edge: "))

    if a == b and b == c and c == d and d == a:
        print("It is a square!")
    elif a == b and c == d:
        print("It is a rectangle!")
    elif a == c and b == d:
        print("It is a rectangle!")
    elif a == d and b == c:
        print("It is a rectangle!")
    else:
        print("It is just a random quadrilateral!")

elif choice == "2":
    a = int(input("Enter first edge: "))
    b = int(input("Enter second edge: "))
    c = int(input("Enter third edge: "))

    if abs(b-c) < a < b+c and abs(a-c) < b < a+c and abs(a-b) < c < a+b:
        if a == b == c:
            print("It is an equilateral triangle!")
        elif a == b or b == c or a == c:
            print("It is an isosceles triangle!")
        else:
            print("It is just a random triangle!")
    else:
        print("Your inputs cannot form triangles due to triangle inequality!")

else:
    print("Your choice is wrong! Please try again!")