matrix = [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
]

for layer in range(len(matrix) // 2):
    first = layer
    last = len(matrix) - 1 - layer
    for i in range(first, last):
        offset = i - first
        temp = matrix[first][i]
        matrix[first][i] = matrix[last - offset][first]
        matrix[last - offset][first] = matrix[last][last - offset]
        matrix[last][last - offset] = matrix[i][last]
        matrix[i][last] = temp

print(matrix)
