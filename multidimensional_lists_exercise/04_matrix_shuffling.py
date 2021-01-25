def read_matrix(x):
    matrix = []
    for _ in range(x):
        row = input().split()
        matrix.append(row)

    return matrix


def print_result(matrix, line):
    is_valid = False
    if line[0] == "swap" and len(line) == 5:
        is_valid = True
        row_1, col_1, row_2, col_2 = [int(line[i]) for i in range(1, 5)]

        try:
            first_element = matrix[row_1][col_1]
            second_element = matrix[row_2][col_2]
            matrix[row_1].pop(col_1)
            matrix[row_1].insert(col_1, second_element)
            matrix[row_2].pop(col_2)
            matrix[row_2].insert(col_2, first_element)
        except:
            is_valid = False

    if is_valid:
        [print(" ".join(row)) for row in matrix]
    else:
        print("Invalid input!")


rows_count, cols_count = [int(el) for el in input().split()]
matrix = read_matrix(rows_count)

command = input()

while not command == "END":
    command_data = command.split()
    print_result(matrix, command_data)
    command = input()