
def permute(s, result):
    if (len(s) == 0):
        results.append(result)
        return

    for i in range(len(s)):
        permute(s[0:i] + s[i + 1:], result + s[i])


# Driver Code
result = ""
results = []

s = input("Enter the string : ")

print("All possible strings are : ")
permute(s, result)
print(results)
print(len(results))
