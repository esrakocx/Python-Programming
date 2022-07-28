print("Welcome to the ATM Machine")
pin = "1223"
chance = 2
balance = 1000

while True:
    user_pin = input("Please enter PIN: ")
    if chance == 0:
        print("Your account was locked!")
        break
    if pin == user_pin:
        chose = input("""Please choose what you want to do.
        1. Remaining balance

        2. Deposit

        3. Withdraw money
        
        4. To exit enter q\nChose: """)

        if chose == "1":
            print("Your balance: {}".format(balance))
        elif chose == "2":
            deposit = int(input("Enter the amount you want to deposit: "))
            balance += deposit
            print("Your balance: {}".format(balance))
        elif chose == "3":
            withdraw = int(input("Enter the amount you want to withdraw: "))

            if withdraw < balance:
                balance -= withdraw
                print("Your balance: {}".format(balance))
                continue
            else:
                print("Insufficient balance")
        elif chose == "q":
            print("Exiting...")
            break
        else:
            print("Invalid transaction")
            continue
    else:
        print("Incorrect PIN")
        chance -= 1
        continue
