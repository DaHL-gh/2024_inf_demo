def func(n):
    if n > 2024:
        return n
    else:
        return n * func(n + 1)

print(func(2022) / func(2024))