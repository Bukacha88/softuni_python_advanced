def is_valid(r, c, l):
    if 0 <= r < l and 0 <= c < l:
        return True
    return False


def find_not_bombs(matrix_1, size):
    for r in range(len(matrix_1)):
        for c in range(len(matrix_1[r])):
            if not matrix_1[r][c] == '*':
                count_near_bombs(matrix_1, r, c, size)
    return matrix_1


def count_near_bombs(the_matrix, row_1, col_1, size):
    moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for i in range(len(moves)):
        curr_row = row_1 + moves[i][0]
        curr_coll = col_1 + moves[i][1]
        if is_valid(curr_row, curr_coll, size):
            if the_matrix[curr_row][curr_coll] == '*':
                the_matrix[row_1][col_1] += 1
    return the_matrix


n = int(input())
matrix = []
for i in range(n):
    matrix.append([0 for x in range(n)])
number_of_bombs = int(input())
for i in range(number_of_bombs):
    (row, col) = input().split(', ')
    row = int(row[1:])
    col = int(col[:-1])
    if row >= 0 and col >= 0:
        matrix[row][col] = '*'

bomb_field = find_not_bombs(matrix,n)
for elements in bomb_field:
    print(*(elements))

