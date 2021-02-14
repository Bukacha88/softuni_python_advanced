from math import floor


def find_santa(matrix_1):
    for i in range(len(matrix_1)):
        for j in range(len(matrix_1[i])):
            if matrix_1[i][j] == "P":
                row = i
                col = j
                return row, col


def is_valid(r, c, matrix_1):
    if 0 <= r < len(matrix_1) and 0 <= c < len(matrix_1):
        return True
    return False


size = int(input())
matrix = []
for _ in range(size):
    matrix.append([x for x in input().split()])
points = 0
current_row, current_col = find_santa(matrix)
game_over = False
moves = []
while points < 100:
    command = input()
    mapper = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1)
    }
    if command in mapper:
        current_row += mapper[command][0]
        current_col += mapper[command][1]
        if is_valid(current_row, current_col, matrix):
            if not matrix[current_row][current_col] == 'X':
                points += int(matrix[current_row][current_col])
                moves.append([current_row, current_col])
            else:
                game_over = True
                break
        else:
            game_over = True
            break
    else:
        continue
if game_over:
    points = floor(points / 2)
    print(f"Game over! You've collected {points} coins.")
    print("Your path:")
    for el in moves:
        print(el)
else:
    print(f"You won! You've collected {points} coins.")
    print("Your path:")
    for el in moves:
        print(el)