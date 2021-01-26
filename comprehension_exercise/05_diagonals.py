size = int(input())
matrix = [[int(j) for j in input().split(', ')] for i in range(size)]
primary_diagonal = [str(matrix[i][i]) for i in range(len(matrix))]
primary_diagonal_sum = sum([int(x) for x in primary_diagonal])
secondary_diagonal =[str(matrix[i][len(matrix)-1-i]) for i in range(len(matrix))]
secondary_diagonal_sum = sum([int(x) for x in secondary_diagonal])
print(f"First diagonal: {', '.join(primary_diagonal)}. Sum: {primary_diagonal_sum}")
print(f"Second diagonal: {', '.join(secondary_diagonal)}. Sum: {secondary_diagonal_sum}")