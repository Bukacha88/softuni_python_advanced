text = list(input())
s = []

for i in range(len(text)):
    s.append(text.pop())

print("".join(s))