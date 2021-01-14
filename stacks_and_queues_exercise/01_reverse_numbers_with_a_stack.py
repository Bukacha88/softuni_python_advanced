numbers = input().split()

stack = []

for _ in range(len(numbers)):
    stack.append(numbers.pop())
print(" ".join(stack))

