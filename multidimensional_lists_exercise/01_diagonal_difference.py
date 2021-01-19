def read_matrix():
    size = int(input())
    matrix = []
    for row_index in range(size):
        row = [int(x) for x in input().split()]
        matrix.append(row)
    return matrix


def get_difference_diagonals(matrix):
    diagonal_sum = 0
    second_diagonal_sum = 0
    size = len(matrix)
    for i in range(len(matrix)):
        diagonal_sum += matrix[i][i]
        second_diagonal_sum += matrix[i][size - i - 1]
    return abs(diagonal_sum - second_diagonal_sum)


print(get_difference_diagonals(read_matrix()))
