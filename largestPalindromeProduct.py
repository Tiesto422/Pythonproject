
def largestPalindromeProduct():
    largest = 0
    isPalindrome = False
    i = 999
    j = 999
    while (i > 900):
        while(j > 900):
            test = str(i * j)
            for k in range(int(len(test)/2)):
                if(test[k] == test[len(test) - 1 - k]):
                    isPalindrome = True
                else:
                    isPalindrome = False
                    break
            if(isPalindrome and largest < int(test)):
                largest = int(test)
            j -= 1
        j = 999
        i -= 1
    return largest


print(largestPalindromeProduct())
