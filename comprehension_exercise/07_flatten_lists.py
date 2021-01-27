matrix = [list(map(int, nums.split())) for nums in input().split('|')]
# [print(*matrix[i], sep=' ', end=' ') for i in range(len(matrix) - 1, -1, -1)]
list_nums = []
for i in range(len(matrix) - 1, -1, -1):
    list_nums += matrix[i]
print(' '.join(map(str, list_nums)))