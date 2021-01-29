def even_odd(*args):
    if args[-1] == "even":

        return list(filter(lambda x: x % 2 == 0, args[0:-1]))
    elif args[-1] == "odd":
        return list(filter(lambda x: x % 2 != 0, args[0:-1]))


print(even_odd(1, 2, 3, 4, 5, 6, "even"))