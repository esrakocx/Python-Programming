import random
import time

print("""
**************************************
~Number Guessing Game~

Please enter a number between 1 and 40.
**************************************

""")

random_number = random.randint(1, 40)
chance = 7

while True:
    guess = int(input("Please enter your guess: "))

    if random_number > guess:
        print("Information is being queried...")
        time.sleep(1)

        print("Please enter a larger number!")
        chance -= 1

    elif random_number < guess:
        print("Information is being queried...")
        time.sleep(1)

        print("Please enter a smaller number!")
        chance -= 1

    else:
        print("Information is being queried...")
        time.sleep(1)
        print("Congratulations! You know!\nNumber is: ",random_number)
        break

    if chance == 0:
        print("Your guess is over!")
        print("Number was: ",random_number)
        break
