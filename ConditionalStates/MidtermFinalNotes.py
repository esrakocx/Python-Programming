print("Find your letter grade using your Midterm and Final notes!\n")

midterm1 = int(input("Your first midterm: "))
midterm2 = int(input("Your second midterm: "))
final = int(input("Your final: "))

avg = midterm1 * 0.3 + midterm2 * 0.3 + final * 0.4
print("Your average note: {}".format(avg))

if avg >= 90:
    print("Your letter grade: AA")
elif avg >= 85:
    print("Your letter grade: BA")
elif avg >= 80:
    print("Your letter grade: BB")
elif avg >= 75:
    print("Your letter grade: CB")
elif avg >= 70:
    print("Your letter grade: CC")
elif avg >= 65:
    print("Your letter grade: DC")
elif avg >= 60:
    print("Your letter grade: DD")
elif avg >= 55:
    print("Your letter grade: FD")
elif avg < 55:
    print("Your letter grade: FF")