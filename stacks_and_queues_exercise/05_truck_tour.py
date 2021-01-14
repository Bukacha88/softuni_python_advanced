from collections import deque

n = int(input())

stations = deque([])

for _ in range(n):
    stations.append(input())

for big_circle_iteration in range(n):
    is_valid = True
    tank_petrol = 0
    for small_circle_iteration in range(n):
        current_station = stations[small_circle_iteration]

        petrol, distance_to_next_station = current_station.split()
        petrol = int(petrol)
        distance_to_next_station = int(distance_to_next_station)
        tank_petrol += petrol - distance_to_next_station

        if tank_petrol < 0:
            is_valid = False
            stations.append(stations.popleft())
            break

    if is_valid:
        print(big_circle_iteration)
        break