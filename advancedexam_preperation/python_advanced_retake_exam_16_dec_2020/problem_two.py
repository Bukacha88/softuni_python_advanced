def is_valid_move(matrix_1, r, c):
    if 0 <= r < len(matrix_1) and 0 <= c < len(matrix_1):
        return True
    return False


string = input()
last_letter = ''
size = int(input())
matrix = []
current_row = 0
current_col = 0
for row_index in range(size):
    matrix.append([x for x in input()])
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 'P':
            current_row = i
            current_col = j
movement_number = int(input())
for _ in range(movement_number):
    command = input()
    if command == 'up':
        if is_valid_move(matrix, current_row - 1, current_col):
            matrix[current_row][current_col] = '-'
            current_row -= 1
            if matrix[current_row][current_col] != '-':

                string += matrix[current_row][current_col]
                matrix[current_row][current_col] = 'P'


        else:
            if len(string) > 0:
                string = string[:-1]

    elif command == 'down':
        if is_valid_move(matrix, current_row + 1, current_col):
            matrix[current_row][current_col] = '-'
            current_row += 1
            if matrix[current_row][current_col] != '-':
                string += matrix[current_row][current_col]
                matrix[current_row][current_col] = 'P'


        else:
            if len(string) > 0:
                string = string[:-1]

    elif command == 'left':
        if is_valid_move(matrix, current_row, current_col - 1):
            matrix[current_row][current_col] = '-'
            current_col -= 1
            if matrix[current_row][current_col] != '-':
                string += matrix[current_row][current_col]
                matrix[current_row][current_col] = 'P'


        else:
            if len(string) > 0:
                string = string[:-1]

    elif command == 'right':
        if is_valid_move(matrix, current_row, current_col + 1):
            matrix[current_row][current_col] = '-'
            current_col += 1
            if matrix[current_row][current_col] != '-':
                string += matrix[current_row][current_col]
                matrix[current_row][current_col] = 'P'


        else:
            if len(string) > 0:
                string = string[:-1]

print(string)
for i in range(len(matrix)):

    print(*[x for x in "".join(matrix[i])], sep='')

