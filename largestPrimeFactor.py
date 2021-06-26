import math


def largestPrimeFactor(num):
    largestPrimeCurr = 0
    for i in range(5, int(math.sqrt(num))):
        if (num % i == 0):
            isPrime = True
            for j in range(2, i):
                if (i % j == 0):
                    isPrime = False
                    break
            if (isPrime):
                largestPrimeCurr = i

    return largestPrimeCurr


print(largestPrimeFactor(13195))
