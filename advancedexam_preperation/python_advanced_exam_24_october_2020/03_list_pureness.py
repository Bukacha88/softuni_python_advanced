import sys


def best_list_pureness(*args):
    list_of_numbers = list(map(int, *args[:-1]))

    n = int(args[-1])
    best_sum = -sys.maxsize
    best_rotation_number = 0
    rotation_number = 0
    if len(list_of_numbers) > 0:
        if n > 0:
            for j in range(n + 1):

                rotation_sum = 0
                for i in range(len(list_of_numbers)):
                    rotation_sum += list_of_numbers[i] * i
                if rotation_sum > best_sum:
                    best_sum = rotation_sum
                    best_rotation_number = j

                list_of_numbers.insert(0, list_of_numbers.pop())
        else:
            rotation_sum = 0
            for i in range(len(list_of_numbers)):
                rotation_sum += list_of_numbers[i] * i
            if rotation_sum > best_sum:
                best_sum = rotation_sum
                best_rotation_number = 0

        return f"Best pureness {best_sum} after {best_rotation_number} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
