print("How much have to you pay for fuel in total?\n")

print("Please enter how much fuel your vehicle consumes per kilometer: ")
fuel = float(input("Fuel:"))

print("Please enter how many kilometers will you travel: ")
km = float(input("Km:"))

total = fuel*km
print("You have to pay {} unit.".format(total))

