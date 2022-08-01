print("~Perfect numbers from 1 to 1000~\n")

def find_perfectnumbers(number):
    total = 0
    for i in range(1, number):
        if number % i == 0:
            total += i
    return total == number

for i in range(1, 1000):
    if find_perfectnumbers(i):
        print(i, "is a perfect number!")
