def stock_availability(boxes: list, command: str, *args):
    if command == 'delivery':
        for el in args:
            boxes.append(el)
    elif command == 'sell':
        if not args:
            boxes.pop(0)
        elif isinstance(args[0], int):
            for i in range(args[0]):
                boxes.pop(0)
        else:
            boxes = [el for el in boxes if el not in args]
    return boxes


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))