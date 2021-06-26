
def sumOfSquares():
    sumOfSquares = 0
    total = 0
    for i in range(1, 101):
        sumOfSquares += i * i
        total += i
    return total * total - sumOfSquares


print(sumOfSquares())
