print("Log in | Sign Up")

choice = input("\nEnter 1 to Log in\nEnter 2 to Sign up\nChoice:")
system_name = "user1"
system_password = "12345"

if choice == "1":
    name = input("Username: ")
    password = input("Password: ")
    if system_name == name and system_password != password:
        print("You entered wrong password! Please try again!")
    elif system_name != name and system_password == password:
        print("You entered wrong username! Please try again!")
    elif system_name != name and system_password != password:
        print("You entered wrong username and password! Please try again!")
    else:
        print("Login successful! Welcome!")
elif choice == "2":
    new_name = input("Username:  ")
    email = input("Email: ")
    new_password = input("Password: ")
    print("\nRegistration successful! Welcome!")
    print("\nYour username: {}\nYour email: {}\nYour password: {}".format(new_name, email, new_password))
