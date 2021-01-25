size = int(input())

rows = size
columns = size
matrix = []
count = 0
max_count = 0
current_count = 0

for i in range(rows):
    matrix.append([])
    matrix[i] += list(input())

while True:
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == 'K':
                try:
                    k = i - 2
                    l = j - 1
                    if matrix[k][l] == 'K' and k >= 0 and l >= 0:
                        current_count += 1
                except:
                    IndexError
                try:
                    k = i - 2
                    l = j + 1
                    if matrix[k][l] == 'K' and k >= 0 and l >= 0:
                        current_count += 1
                except:
                    IndexError
                try:
                    k = i + 2
                    l = j - 1
                    if matrix[k][l] == 'K' and k >= 0 and l >= 0:
                        current_count += 1
                except:
                    IndexError
                try:
                    k = i + 2
                    l = j + 1
                    if matrix[k][l] == 'K' and k >= 0 and l >= 0:
                        current_count += 1
                except:
                    IndexError
                try:
                    k = i - 1
                    l = j - 2
                    if matrix[k][l] == 'K' and k >= 0 and l >= 0:
                        current_count += 1
                except:
                    IndexError
                try:
                    k = i - 1
                    l = j + 2
                    if matrix[k][l] == 'K' and k >= 0 and l >= 0:
                        current_count += 1
                except:
                    IndexError
                try:
                    k = i + 1
                    l = j - 2
                    if matrix[k][l] == 'K' and k >= 0 and l >= 0:
                        current_count += 1
                except:
                    IndexError
                try:
                    k = i + 1
                    l = j + 2
                    if matrix[k][l] == 'K' and k >= 0 and l >= 0:
                        current_count += 1
                except:
                    IndexError

            if current_count > max_count:
                max_count = current_count
                row_index = i
                column_index = j
            current_count = 0

    if max_count:
        matrix[row_index][column_index] = 'O'
        count += 1
        max_count = 0
    else:
        print(count)
        break
