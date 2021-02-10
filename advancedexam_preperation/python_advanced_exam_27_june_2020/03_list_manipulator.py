from collections import deque


def list_manipulator(numbers, command, *sub_command):
    numbers = deque([int(el) for el in numbers])

    if command == 'add':
        add_numbers = list(map(int, sub_command[1:]))
        if sub_command[0] == 'beginning':
            for el in add_numbers[::-1]:
                numbers.appendleft(el)
        else:
            for el in add_numbers:
                numbers.append(el)
    elif command == 'remove':
        if sub_command[0] == 'beginning':
            if sub_command[1:]:
                remove_numbers = list(map(int, sub_command[1:]))
                for el in remove_numbers:
                    for i in range(el):
                        numbers.popleft()
            else:
                numbers.popleft()
        elif sub_command[0] == 'end':
            if sub_command[1:]:
                remove_numbers = list(map(int, sub_command[1:]))
                for el in remove_numbers:
                    for i in range(el):
                        numbers.pop()
            else:
                numbers.pop()
    return list(numbers)


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
