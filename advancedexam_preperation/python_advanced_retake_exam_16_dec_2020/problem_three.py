def get_magic_triangle(n):
    matrix = [[1], [1, 1]]
    for i in range(2, n):
        matrix.append([])
        for j in range(i + 1):
            if j == 0:
                matrix[i].append(matrix[i - 1][j])
            elif 0 < j < i:
                matrix[i].append(matrix[i - 1][j - 1] + matrix[i - 1][j])
            elif j == i:
                matrix[i].append(matrix[i - 1][j - 1])
    return matrix


print(get_magic_triangle(5))