def is_valid_move(matrix_1, r, c):
    if 0 <= r < len(matrix_1) and 0 <= c < len(matrix_1):
        return True
    return False


def get_new_pos(command, curr_pos):
    new_row, new_col = curr_pos[0], curr_pos[1]
    if command == "up":
        new_row -= 1
    elif command == "down":
        new_row += 1
    elif command == "right":
        new_col += 1
    elif command == "left":
        new_col -= 1
    return new_row, new_col


def search_matrix(matrix, size, search):
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == search:
                return row, col


n = int(input())
matrix = []
burrows = {'burrow_1': [], 'burrow_2': []}

game_over = False
for row_index in range(n):
    matrix.append([x for x in input()])
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 'B':
            if len(burrows['burrow_1']) > 0:
                burrows['burrow_2'].append(i)
                burrows['burrow_2'].append(j)
            else:
                burrows['burrow_1'].append(i)
                burrows['burrow_1'].append(j)

snake_pos = search_matrix(matrix, n, "S")
food_eaten = 0
while food_eaten < 10:
    command = input()
    new_row, new_col = get_new_pos(command, snake_pos)

    if is_valid_move(matrix, new_row, new_col):
        if matrix[new_row][new_col] == 'B':
            matrix[new_row][new_col] = '.'

            if new_row == burrows['burrow_1'][0] and new_col == burrows['burrow_1'][1]:
                new_row = burrows['burrow_2'][0]
                new_col = burrows['burrow_2'][1]



            elif new_row == burrows['burrow_2'][0] and new_col == burrows['burrow_2'][1]:
                new_row = burrows['burrow_1'][0]
                new_col = burrows['burrow_1'][1]
        if matrix[new_row][new_col] == '*':
            food_eaten += 1
        matrix[new_row][new_col] = "S"
        matrix[snake_pos[0]][snake_pos[1]] = "."
        snake_pos = search_matrix(matrix, n, "S")
    else:
        matrix[snake_pos[0]][snake_pos[1]] = "."
        game_over = True
        break

if game_over:
    print("Game over!")
else:
    print("You won! You fed the snake.")
print(f"Food eaten: {food_eaten}")
for i in range(len(matrix)):
    print(*[x for x in "".join(matrix[i])], sep='')
