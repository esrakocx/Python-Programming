print("""
******************

User Login Screen

******************
""")

system_name = "user1"
system_password = "12345"
login_chance = 2
check = 282

while True:
    name = input("Username: ")
    password = input("Password: ")

    if login_chance == 0:
        print("Your chance to login is over!")
        break
    if system_name != name and system_password == password:
        print("Incorrect username!")
        login_chance -= 1
    elif system_name == name and system_password != password:
        print("Incorrect password!")
        response = input("Forgot password? Y/N ")
        login_chance -= 1
        if response == "Y" or response == "y":
            print("We sent a code to your account for password reset.")
            code = int(input("Code: "))
            if code == check:
                new_password = input("New password: ")
                system_password = new_password
                continue
            else:
                print("Try Again! Check your code!")
        elif response == "N" or response == "n":
            print("Please try again then!")
            continue
        else:
            print("Incorrect input!")
            continue
    elif system_name != name and system_password != password:
        print("Incorrect password and user name!")
        login_chance -= 1
    else:
        print("Welcome!")
        login_chance -= 1
        break
