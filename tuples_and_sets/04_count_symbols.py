text = tuple(map(str, input()))
occur = {}

for char in text:
    if char not in occur:
        occur[char] = 0
    occur[char] += 1

for key, values in sorted(occur.items()):
    print(f"{key}: {values} time/s")