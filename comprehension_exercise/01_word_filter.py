word_filter = [el for el in input().split() if len(el) % 2 == 0]
for word in word_filter:
    print(word)