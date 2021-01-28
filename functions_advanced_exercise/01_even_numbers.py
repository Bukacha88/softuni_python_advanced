numbers = [int(el) for el in input().split()]
numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(numbers)