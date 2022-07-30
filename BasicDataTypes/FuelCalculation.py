print("How much have to you pay for fuel in total?\n")

fuel = float(input("Please enter how much fuel your vehicle consumes per kilometer: "))
km = float(input("Please enter how many kilometers will you travel: "))

total = fuel * km
print("You have to pay {} unit.".format(total))

