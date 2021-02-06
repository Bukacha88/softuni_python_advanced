numbers = [int(el) for el in input().split(', ')]
index = int(input())

number = numbers[index]
count_number = numbers.count(number)

numbers = sorted(numbers)

cycles = 0
for el in range(len(numbers)):

    if not numbers[el] == number:
        cycles += numbers[el]
    elif numbers[el] == number:
        cycles += (count_number * number)
        break
print(cycles)
