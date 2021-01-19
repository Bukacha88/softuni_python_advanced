def read_matrix():
    rows_count, columns_count = map(int, input().split(' '))
    matrix = []
    for row_index in range(rows_count):
        row = [x for x in input().split()]
        matrix.append(row)
    return matrix


def find_squares(matrix):
    submatrix_size = 2
    squares_count = 0
    for row_index in range(len(matrix) - submatrix_size + 1):
        for col_index in range(len(matrix[row_index]) - submatrix_size + 1):
            squares = set()
            for r in range(row_index, row_index + submatrix_size):
                for c in range(col_index, col_index + submatrix_size):
                    squares.add(matrix[r][c])
            if len(squares) == 1:
                squares_count += 1
    return squares_count

matrix = read_matrix()

print(find_squares(matrix))


