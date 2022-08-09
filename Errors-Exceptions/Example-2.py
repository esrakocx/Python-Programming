# Even numbers in the list

def find_evens(number):
    if number % 2 == 0:
        return number
    else:
        raise ValueError


numbers = [121, 34, 65, 78, 90, 1, 57, 83, 51, 44, 1006]

for i in numbers:
    try:
        print(find_evens(i))
    except ValueError:
        pass
