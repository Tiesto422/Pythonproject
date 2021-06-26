
def multipleOfThreeAndFive(num):
    sumOfFactors = 0
    i = 1
    while(i < num):
        if(i % 3 == 0 or i % 5 == 0):
            sumOfFactors += i
        i += 1

    return sumOfFactors


print(multipleOfThreeAndFive(1000))
