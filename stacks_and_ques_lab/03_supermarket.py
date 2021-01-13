from collections import deque
end_command = 'End'
paid_command = 'Paid'
queue = deque()
while True:
    command = input()
    if command == paid_command:
        while queue:
            print(queue.popleft())
    elif command == end_command:
        print(f"{len(queue)} people remaining.")
        break
    else:
        queue.append(command)

