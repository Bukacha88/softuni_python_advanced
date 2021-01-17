n = int(input())
longest_intersection = set([])
len_longest_intersection = 0
for _ in range(n):
    data = input().split('-')
    first_intersection = data[0].split(',')
    first_start = int(first_intersection[0])
    first_end = int(first_intersection[1])
    second_intersection = data[1].split(',')
    second_start = int(second_intersection[0])
    second_end = int(second_intersection[1])
    a = set([])
    b = set([])
    for i in range(first_start, first_end + 1):
        a.add(i)
    for j in range(second_start, second_end + 1):
        b.add(j)
    intersection = a.intersection(b)
    if len(intersection) > len_longest_intersection:
        len_longest_intersection = len(intersection)
        longest_intersection = intersection

print(f"Longest intersection is {list(longest_intersection)} with length {len_longest_intersection}")



