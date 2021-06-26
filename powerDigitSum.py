

def power2DigitSum(num):
    sumOfDigits = 0
    newNum = str(pow(2, num))
    for i in newNum:
        sumOfDigits += int(i)
    return sumOfDigits


print(power2DigitSum(15))
print(power2DigitSum(1000))
