n = int(input())
unique_elements = set([])
for _ in range(n):
    elements = input().split()
    for element in elements:
        unique_elements.add(element)
for el in unique_elements:
    print(el)
