def func(start, end):
    if start > end:
        return 0
    elif start == end:
        return 1

    if start == 11:
        return 0

    return func(start + 1, end) + func(start * 2, end) + func(start ** 2, end)

print(func(2, 20))