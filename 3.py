def func(n):
    if n % 3 == 0:
        n = n * 8 + n % 8
    else:
        n = int(bin(n)[2:] + bin(n % 3 * 3)[2:], 2)

    return n

print(func(21))
