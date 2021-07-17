input = [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
]
matrix = [[0 for x in range(len(input[0]))] for y in range(len(input))]
for i in range(len(input)):
    for j in range(len(input[0])):
        matrix[j][len(input) - 1 - i] = input[i][j]
print(matrix)
