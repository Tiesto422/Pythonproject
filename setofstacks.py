class stacks:
    def __init__(self):
        self.stack = []

    def push(self, value: int):
        self.stack.append(value)

    def peek(self):
        return self.stack[-1]

    def pop(self):
        value = self.stack[-1]
        self.stack.pop()
        return value

    def print(self):
        print(self.stack)

    def len(self):
        return len(self.stack)


input = stacks()
input.push(8)
input.push(9)
input.push(5)
input.push(2)
input.push(4)
input.push(7)
input.push(0)
input.push(1)
input.push(3)
input.push(6)

print("Original")
input.print()
result = stacks()

while input.len() > 0:
    temp = input.pop()
    while result.len() > 0 and result.peek() > temp:
        input.push(result.pop())
    result.push(temp)
input.print()
result.print()
