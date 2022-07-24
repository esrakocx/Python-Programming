print("Please enter your name: ")
name = input("Name: ")

print("Please enter your surname: ")
surname = input("Surname: ")

print("Please enter your number: ")
number = input("Number: ")

info=[name, surname, number]

print("Your name is: {}\nYour surname is: {}\nYour number is: {}".format(info[0], info[1], info[2]))