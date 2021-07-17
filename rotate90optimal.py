matrix = [[2, 3, 1, 4], [7, 8, 5, 3], [3, 3, 2, 1], [9, 0, 8, 3]]
print('\n'.join([' '.join([str(cell) for cell in row]) for row in matrix]))
for layer in (range(len(matrix) // 2)):
    first = layer
    last = len(matrix) - 1 - layer
    for i in range(first, last):
        offset = i - first
        temp = matrix[first][i]
        matrix[first][i] = matrix[last-offset][first]
        matrix[last - offset][first] = matrix[last][last - offset]
        matrix[last][last-offset] = matrix[i][last]
        matrix[i][last] = temp
print("Result = ")
print('\n'.join([' '.join([str(cell) for cell in row]) for row in matrix]))
