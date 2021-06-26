
input = [[0, 0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 1, 1, 0], [0, 0, 1, 1, 0, 0, 0], [
    0, 0, 1, 1, 1, 1, 0], [0, 0, 0, 1, 1, 1, 0], [0, 0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0]]
print("Array to Test")
print('\n'.join([' '.join([str(cell) for cell in row]) for row in input]))
memo = [[0] * (len(input[0]) + 1) for _ in range(len(input) + 1)]
print("Result")

maxBoxSize = 0
for rowIndex, row in enumerate(input):
    for colIndex, value in enumerate(row):
        if value == 1:
            boxLimit = memo[rowIndex][colIndex] + 1
            i = rowIndex
            j = colIndex
            while value < boxLimit:
                if memo[i][colIndex + 1] > 0 and memo[rowIndex + 1][j] > 0:
                    value += 1
                else:
                    break
                i -= 1
                j -= 1
            if value > maxBoxSize:
                maxBoxSize = value
            memo[rowIndex + 1][colIndex + 1] = value

print('\n'.join([' '.join([str(cell) for cell in row]) for row in memo]))

print("Final Result = " + str(maxBoxSize))
