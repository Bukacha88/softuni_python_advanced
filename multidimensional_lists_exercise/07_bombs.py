n = int(input())
the_matrix = []
for _ in range(n):
    the_matrix.append([int(x) for x in input().split()])




def get_bombs():
    the_bombs = []

    for bomb in input().split():
        if bomb:
            the_bombs.append([int(x) for x in bomb.split(",")])

    return the_bombs


def is_valid( r, c,l):
    if 0 <= r < l and 0 <= c < l:
        return True
    return False


def explosion(matrix_1, row_1, col_1,size):
    moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    bomb = matrix_1[row_1][col_1]
    if bomb > 0:

        matrix_1[row_1][col_1] = 0


        for i in range(len(moves)):
            curr_row = row_1 + moves[i][0]
            curr_coll = col_1 + moves[i][1]
            if is_valid( curr_row, curr_coll,size):
                if matrix_1[curr_row][curr_coll] > 0:
                    matrix_1[curr_row][curr_coll] -= bomb

    return matrix_1


def alive_cells_finder(matrix_1):
    counter = 0
    the_sum = 0

    for r in range(len(matrix_1)):
        for c in range(len(matrix_1[r])):
            if matrix_1[r][c] > 0:
                counter += 1
                the_sum += matrix_1[r][c]

    return counter, the_sum


def print_matrix(matrix_1):
    for r in matrix_1:
        print(" ".join(str(x) for x in r))


matrix = the_matrix
bombs = get_bombs()

for row, col in bombs:
    explosion(matrix, row, col,n)

result = alive_cells_finder(matrix)
print(f"Alive cells: {result[0]}")
print(f"Sum: {result[1]}")
print_matrix(matrix)