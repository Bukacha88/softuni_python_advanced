def func_executor(*args):
    results = []
    for func_name, data in args:
        res = func_name(*data)
        results.append(res)
    return results
