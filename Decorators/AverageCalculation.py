def extra(func):
    def wrapper(nums):
        even_nums = 0
        total_evens = 0
        odd_nums = 0
        total_odds = 0

        for num in nums:
            if num % 2 == 0:
                even_nums += 1
                total_evens += num
            else:
                odd_nums += 1
                total_odds += num

        print("The average of even numbers: {}".format(total_evens/even_nums))
        print("The average of odd numbers: {}".format(total_odds/odd_nums))
        func(nums)
    return wrapper


@extra
def cal_avr(nums):

    total = 0
    for num in nums:
        total += num

    print("General average: ", total/len(nums))


cal_avr([1, 2, 3, 4, 65, 86, 34, 90, 44, 56])
