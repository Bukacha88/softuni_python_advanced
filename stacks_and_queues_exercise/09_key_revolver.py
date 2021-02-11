from collections import deque

bullet_price = int(input())
size_gun = int(input())
bullets = list(map(int, input().split()))
locks = deque(list(map(int, input().split())))
value_of_intelligence = int(input())
bullets_used = 0
barrel_reload = 0
no_bullets = False
while locks:
    if bullets[-1] <= locks[0]:
        bullets.pop()
        locks.popleft()
        print("Bang!")
    else:
        bullets.pop()
        print("Ping!")
    bullets_used += 1
    barrel_reload += 1
    if barrel_reload == size_gun and len(bullets) > 0:
        barrel_reload = 0
        print("Reloading!")
    if len(bullets) == 0 and len(locks) > 0:
        no_bullets = True
        break
earned = value_of_intelligence - bullets_used * bullet_price
if no_bullets:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${earned}")
