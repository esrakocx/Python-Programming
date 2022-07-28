print("~Factorial Calculator~\n")
print("To exit enter q.\n")

while True:
    number = input("Enter the number whose factorial you want to find: ")

    if number == "q":
        print("Exiting...")
        break
    else:
        number = int(number)
        fact = 1

        for i in range(2, number+1):
            fact *= i
        print("{}! = {}".format(number, fact))
