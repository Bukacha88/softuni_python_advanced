matrix = []
queens = []
kings_row = 0
kings_col = 0
for row_index in range(8):
    matrix.append([x for x in input().split()])
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 'K':
            kings_row = i
            kings_col = j
current_row = kings_row
current_col = kings_col
if current_col < 7:
    while current_col < 7:
        current_col += 1
        if matrix[current_row][current_col] == 'Q':
            queens.append([current_row, current_col])
            break
current_row = kings_row
current_col = kings_col
if current_col > 0:
    while current_col > 0:
        current_col -= 1
        if matrix[current_row][current_col] == 'Q':
            queens.append([current_row, current_col])
            break
current_row = kings_row
current_col = kings_col
if current_row < 7:
    while current_row < 7:
        current_row += 1
        if matrix[current_row][current_col] == 'Q':
            queens.append([current_row, current_col])
            break
current_row = kings_row
current_col = kings_col
if current_row > 0:
    while current_row > 0:
        current_row -= 1
        if matrix[current_row][current_col] == 'Q':
            queens.append([current_row, current_col])
            break
current_row = kings_row
current_col = kings_col
if current_row < 7 and current_col < 7:
    while current_row < 7 and current_col < 7:
        current_row += 1
        current_col += 1
        if matrix[current_row][current_col] == 'Q':
            queens.append([current_row, current_col])
            break
current_row = kings_row
current_col = kings_col
if current_row > 0 and current_col > 0:
    while current_row > 0 and current_col > 0:
        current_row -= 1
        current_col -= 1
        if matrix[current_row][current_col] == 'Q':
            queens.append([current_row, current_col])
            break
current_row = kings_row
current_col = kings_col
if current_row > 0 and current_col < 7:
    while current_row > 0 and current_col < 7:
        current_row -= 1
        current_col += 1
        if matrix[current_row][current_col] == 'Q':
            queens.append([current_row, current_col])
            break
current_row = kings_row
current_col = kings_col
if current_row < 7 and current_col > 0:
    while current_row < 7 and current_col > 0:
        current_row += 1
        current_col -= 1
        if matrix[current_row][current_col] == 'Q':
            queens.append([current_row, current_col])
            break


if queens:
    for queen in queens:
        print(queen)
else:
    print("The king is safe!")
