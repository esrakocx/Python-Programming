#Find the elements in the list that contain only numbers

list = ["282", "oh no!", "324e", "ok", "23", "1001", "Apollo 12"]

for i in list:

    try:
        i = int(i)
        print(i, "is a number!")
    except:
        pass

