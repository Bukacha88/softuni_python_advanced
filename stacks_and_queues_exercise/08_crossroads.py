from collections import deque

green_duration = int(input())
free_window_duration = int(input())
needed_passing_time = green_duration + free_window_duration
waiting_cars = deque()
total_passed_cars = 0
is_hit = False


command = input()
while not command == "END":
    curr_passing_time = 0

    if command == "green":
        while waiting_cars and green_duration > curr_passing_time:
            car = waiting_cars[0]
            for char in car:
                curr_passing_time += 1
                if curr_passing_time > needed_passing_time:
                    print("A crash happened!")
                    print(f"{car} was hit at {char}.")
                    is_hit = True
                    break
            total_passed_cars += 1
            waiting_cars.popleft()

    else:
        waiting_cars.append(command)

    if is_hit:
        break
    command = input()
else:
    print("Everyone is safe.")
    print(f"{total_passed_cars} total cars passed the crossroads.")