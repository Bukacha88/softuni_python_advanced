def find_santa(matrix_1):
    for i in range(len(matrix_1)):
        for j in range(len(matrix_1[i])):
            if matrix_1[i][j] == SANTA:
                row = i
                col = j
                return row, col


def find_nice_kids(matrix_1):
    count = 0
    for i in range(len(matrix_1)):
        for j in range(len(matrix_1[i])):
            if matrix_1[i][j] == GOOD_KID:
                count += 1

    return count


def is_valid(r, c, matrix_1):
    if 0 <= r < len(matrix_1) and 0 <= c < len(matrix_1):
        return True
    return False


SANTA = 'S'
GOOD_KID = 'V'
NAUGHTY_KID = 'X'
COOKIES = 'C'
count_presents = int(input())
size_matrix = int(input())
matrix = []
for _ in range(size_matrix):
    matrix.append([x for x in input().split()])
nice_kids = find_nice_kids(matrix)

current_row, current_col = find_santa(matrix)
command = input()
finished_presents = False
while not command == 'Christmas morning':

    mapper = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1)
    }
    if command in mapper:
        if is_valid(current_row, current_col, matrix):
            previous_row = current_row
            previous_col = current_col
            current_row += mapper[command][0]
            current_col += mapper[command][1]
            if matrix[current_row][current_col] == GOOD_KID:
                count_presents -= 1
                matrix[previous_row][previous_col] = '-'
                matrix[current_row][current_col] = 'S'

            elif matrix[current_row][current_col] == NAUGHTY_KID:
                matrix[previous_row][previous_col] = '-'

            elif matrix[current_row][current_col] == '-':
                matrix[current_row][current_col] = 'S'
                matrix[previous_row][previous_col] = '-'
            elif matrix[current_row][current_col] == COOKIES:
                matrix[current_row][current_col] = 'S'
                matrix[previous_row][previous_col] = '-'
                for key in mapper:
                    if is_valid(current_row + mapper[key][0], current_col + mapper[key][1], matrix):
                        previous_row = current_row
                        previous_col = current_col
                        if matrix[current_row + mapper[key][0]][current_col + mapper[key][1]] == GOOD_KID:

                            count_presents -= 1
                            matrix[current_row + mapper[key][0]][current_col + mapper[key][1]] = '-'

                        elif matrix[current_row + mapper[key][0]][current_col + mapper[key][1]] == NAUGHTY_KID:

                            count_presents -= 1
                            matrix[current_row + mapper[key][0]][current_col + mapper[key][1]] = '-'
                        elif matrix[current_row + mapper[key][0]][current_col + mapper[key][1]] == COOKIES:
                            matrix[current_row + mapper[key][0]][current_col + mapper[key][1]] = '-'

                if count_presents <= 0:
                    finished_presents = True
                    break
    if count_presents <= 0:
        finished_presents = True
        break

    command = input()

if count_presents <= 0:
    print("Santa ran out of presents!")

for i in range(len(matrix)):
    print(*[x for x in "".join(matrix[i])], sep='')
if find_nice_kids(matrix) > 0:
    print(f"No presents for {find_nice_kids(matrix)} nice kid/s.")
else:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
