
def evenlyDivisible():
    return 2*2*2*2*3*3*5*7*11*13*17*19


"""
    i = 1
    while (i < 300000000):
        isDivisible = True
        for j in range(2, 21):
            if (i % j != 0):
                isDivisible = False
                break
        if (isDivisible):
            return i
        i += 1
    return 0
"""

print(evenlyDivisible())
