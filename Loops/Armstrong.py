print("Is it an Armstrong number?")

number = input("Number: ")
total = 0
i = 0
while i < len(number):
    total += int(number[i]) ** len(number)
    i += 1

if total == int(number):
    print("{} is an Armstrong number!".format(number))
else:
    print("{} is not an Armstrong number!".format(number))

