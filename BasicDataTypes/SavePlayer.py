print("~Player Registration Program~")

name = input("Player's Name: ")
surname = input("Player's Surname: ")
team = input("Player's Team: ")

info = [name, surname, team]

print("\nInformation is being saved...\n")

print("Player's Name: {}\nPlayer's Surname: {}\nPlayer's Team: {}\n".format(info[0], info[1], info[2]))

print("Player's information saved!")
