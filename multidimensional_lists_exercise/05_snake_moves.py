from collections import deque

rows, columns = map(int, input().split())
snake = deque(list(input()))

matrix = []
for i in range(rows):
    matrix.append([])
    for j in range(columns):
        matrix[i].append(0)

for i in range(rows):
    if i == 0:
        for j in range(columns):
            snake_part = snake.popleft()
            snake.append(snake_part)
            matrix[i][j] = snake_part
    elif i % 2 == 0:
        for j in range(columns):
            snake_part = snake.popleft()
            snake.append(snake_part)
            matrix[i][j] = snake_part
    elif not i % 2 == 0:
        for j in range(columns - 1, -1, -1):
            snake_part = snake.popleft()
            snake.append(snake_part)
            matrix[i][j] = snake_part

[print(*row, sep='') for row in matrix]