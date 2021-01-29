command = input()
numbers = list(map(int, input().split()))
if command == 'Odd':

    print(f"{(sum(filter(lambda x: x % 2 != 0, numbers))) * len(numbers)}")
elif command == 'Even':
    print(f"{(sum(filter(lambda x: x % 2 == 0, numbers))) * len(numbers)}")
