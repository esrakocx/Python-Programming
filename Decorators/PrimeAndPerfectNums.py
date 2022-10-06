def perfect_nums(func):
    def wrapper():
        print("Perfect Numbers: ")
        for number in range(1, 1001):
            i = 1
            total = 0
            while i < number:
                if number % i == 0:
                    total += i
                i += 1
            if total == number:
                print(number)
        func()
    return wrapper


@perfect_nums
def find_prime():
    print("Prime Numbers: ")
    for number in range(2, 1001):
        i = 2
        control = 0
        while i < number:
            if number % i == 0:
                control += 1
            i += 1

        if control == 0:
            print(number)


find_prime()
