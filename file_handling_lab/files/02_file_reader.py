with open('numbers.txt', 'r') as file:
    print(sum([int(el.strip()) for el in file.readlines()]))
