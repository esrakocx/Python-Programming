print("How to pronounce your number?\n")

ones = ["", "bir", "iki"," üç", "dört", "beş", "altı","yedi", "sekiz", "dokuz"]
tens = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]

def pronunciation(number):
    first = number // 10
    second = number % 10

    return tens[first] + " " + ones[second]

while True:
    number = int(input("Number: "))
    print(pronunciation(number))
