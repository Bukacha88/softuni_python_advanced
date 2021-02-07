from collections import Counter


def numbers_searching(*args):
    duplicate_numbers = {}
    list_of_numbers = list(map(int, args))
    min_num = min(list_of_numbers)
    max_num = max(list_of_numbers)
    for el in list_of_numbers:
        if el in duplicate_numbers:
            duplicate_numbers[el] += 1
        else:
            duplicate_numbers[el] = 0
    list_of_duplicate_numbers = []
    for key, value in duplicate_numbers.items():
        if value >= 1:
            list_of_duplicate_numbers.append(key)

    dic = Counter(list_of_numbers)
    missing_number = [i for i in range(min_num, max_num) if dic[i] == 0]
    missing_number.append(sorted(list_of_duplicate_numbers))
    return missing_number
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))