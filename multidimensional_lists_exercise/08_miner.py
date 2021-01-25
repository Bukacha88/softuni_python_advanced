def is_valid_move(matrix_1,r,c):
    if 0 <= r < len(matrix_1) and 0 <= c < len(matrix_1):
        return True
    return False


n = int(input())
commands = input().split()
matrix = []
current_row = 0
current_col = 0
coal_counter = 0
coal_number = 0
game_over = False
is_finished = False
for _ in range(n):
    matrix.append([x for x in input().split()])
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 's':
            current_row = i
            current_col = j
        elif matrix[i][j] == 'c':
            coal_number += 1
for command in range(len(commands)):
    if commands[command] == 'up':
        if is_valid_move(matrix, current_row - 1, current_col):
            current_row -= 1
            if matrix[current_row][current_col] == 'c':
                coal_counter += 1
                matrix[current_row][current_col] = '*'
                if coal_counter == coal_number:
                    is_finished = True

                    break
            elif matrix[current_row ][current_col] == 'e':
                game_over = True
                break
    elif commands[command] == 'down':
        if is_valid_move(matrix, current_row + 1, current_col):
            current_row += 1
            if matrix[current_row][current_col] == 'c':
                coal_counter += 1
                matrix[current_row][current_col] = '*'
                counter = 0
                if coal_counter == coal_number:
                    is_finished = True
                    break
            elif matrix[current_row][current_col] == 'e':
                game_over = True
                break
    elif commands[command] == 'right':
        if is_valid_move(matrix, current_row, current_col + 1):
            current_col += 1
            if matrix[current_row][current_col] == 'c':
                coal_counter += 1
                matrix[current_row][current_col] = '*'
                if coal_counter == coal_number:
                    is_finished = True
                    break
            elif matrix[current_row][current_col] == 'e':
                game_over = True
                break

    elif commands[command] == 'left':
        if is_valid_move(matrix, current_row, current_col - 1):
            current_col -= 1
            if matrix[current_row][current_col] == 'c':
                coal_counter += 1
                matrix[current_row][current_col] = '*'
                if coal_counter == coal_number:
                    is_finished = True
                    break
            elif matrix[current_row][current_col] == 'e':
                game_over = True
                break
if game_over:
    print(f"Game over! ({current_row}, {current_col})")
elif is_finished:
    print(f"You collected all coals! ({current_row}, {current_col})")
else:
    print(f"{coal_counter} coals left. ({current_row}, {current_col})")