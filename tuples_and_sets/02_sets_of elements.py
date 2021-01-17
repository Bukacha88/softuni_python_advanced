n, m = input().split()
n = int(n)
m = int(m)
a = set([])
b = set([])
for _ in range(n):
    a.add(input())
for _ in range(m):
    b.add(input())
c = a.intersection(b)
for digit in c:
    print(digit)
