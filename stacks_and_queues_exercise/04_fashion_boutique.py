s = list(map(int, input().split()))
rack_capacity = int(input())

current_capacity = 0
racks = 1

while s:
    cloth = s.pop()

    if current_capacity + cloth > rack_capacity:
        current_capacity = 0
        racks += 1

    current_capacity += cloth

print(racks)
