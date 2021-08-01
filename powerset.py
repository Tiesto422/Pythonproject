array = [1, 2, 3]
powerset = [[]]
for i in range(len(array)):
    for j in range(len(powerset)):
        powerset.append(powerset[j] + [array[i]])

print(powerset)
