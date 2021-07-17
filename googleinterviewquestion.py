def add_one(input):
    for i in reversed(range(len(input))):
        if input[i] == 9:
            input[i] = 0
        else:
            input[i] += 1
            return input
    result = [0] * (len(input) + 1)
    result[0] = 1
    return result


array = [9, 9, 8]
print(add_one(array))
