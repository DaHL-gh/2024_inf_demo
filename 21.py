def func(rock_c, move_n=-1):
    if rock_c > 128:
        if move_n == 0:
            return 0
        elif move_n == 1:
            return 1
        elif move_n == 2:
            return 0
        elif move_n == 3:
            return 1
        return 0

    if move_n == -1:
        return func(rock_c + 1, move_n + 1) and func(rock_c * 2, move_n + 1)
    elif move_n == 0:
        return func(rock_c + 1, move_n + 1) or func(rock_c * 2, move_n + 1)
    elif move_n == 1:
        return func(rock_c + 1, move_n + 1) and func(rock_c * 2, move_n + 1)
    elif move_n == 2:
        return func(rock_c + 1, move_n + 1) or func(rock_c * 2, move_n + 1)
    else:
        return 0


for x in range(1, 129):
    if func(x):
        print(x)
