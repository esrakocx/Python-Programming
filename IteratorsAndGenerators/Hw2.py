def primes():
    for i in range(2, 1001):
        flag = 1
        for j in range(2, int(i/2) + 1):
            if i % j == 0:
                flag = 0
                break

        if flag == 1:
           yield i


for k in primes():
    print(k)
