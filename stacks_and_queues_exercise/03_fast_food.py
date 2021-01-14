from collections import deque

food = int(input())
orders = deque(list(map(int, input().split())))

print(max(orders))

while orders:
    if orders[0] <= food:
        food -= orders[0]
        orders.popleft()
    else:
        orders = list(map(str, orders))
        print(f"Orders left: {' '.join(orders)}")
        break

if not orders:
    print(f'Orders complete')