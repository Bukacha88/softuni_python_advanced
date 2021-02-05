from collections import deque
males = list(map(int, input().split()))
females = deque([int(el) for el in input().split()])
match_count = 0
while len(males) > 0 and len(females) > 0:

    if males[-1] <= 0:
        males.pop()
        continue
    if females[0] <= 0:
        females.popleft()
        continue
    if males[-1] % 25 == 0:
        males.pop()
        if len(males) > 0:
            males.pop()
            continue
        else:
            break
    if females[0] % 25 == 0:
        females.popleft()
        if len(females) > 0:
            females.popleft()
            continue
        else:
            break
    if males[-1] == females[0]:
        match_count += 1
        males.pop()
        females.popleft()

    else:
        males[-1] -= 2
        females.popleft()

print(f"Matches: {match_count}")
if len(females) == 0 and len(males) > 0:
    print(f"Males left: {', '.join(str(el) for el in males[::-1])}")
    print("Females left: none")
elif len(males) == 0 and len(females) > 0:
    print("Males left: none")
    print(f"Females left: {', '.join(str(el) for el in females)}")
elif len(males) == 0 and len(females) == 0:
    print("Males left: none")
    print("Females left: none")
