
def evenFibonacci():
    sumOfEvenNums = 0
    i = 1
    j = 2
    while (i < 4000000 or j < 4000000):
        if (i % 2 == 0):
            sumOfEvenNums += i
        if (j % 2 == 0):
            sumOfEvenNums += j
        i += j
        j += i

    return sumOfEvenNums


print(evenFibonacci())
