n = int(input())
rows = n
columns = n
matrix = [(list(map(int, input().split()))) for i in range(rows)]

while True:
    line = input()
    if line == 'END':
        break
    command, row, column, value = line.split()
    row = int(row)
    column = int(column)
    value = int(value)
    if 0 <= row <= rows - 1 and 0 <= column <= columns - 1:
        if command == 'Add':
            matrix[row][column] += value
        elif command == 'Subtract':
            matrix[row][column] -= value
    else:
        print('Invalid coordinates')

[print(*row, sep=' ') for row in matrix]