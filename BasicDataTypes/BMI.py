print("~Body Mass Index Calculator~\n")

height = float(input("Please enter your height(m): "))
weight = float(input("Please enter your weight(kg): "))

index = weight / (height * height)
print("Your BMI is: {}".format(index))

if index < 18.5:
    print("Underweight!")
elif 18.5 < index < 24.9:
    print("Normal!")
elif 25 < index < 29.9:
    print("Overweight!")
elif 30 < index < 34.9:
    print("Mild (Class 1) Obesity!")
elif 35 < index < 39.9:
    print("Moderate (Class 2) Obesity!")
elif index >= 40:
    print("Morbid (Class 3) Obesity!")