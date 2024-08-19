
def from_some_count_sys(num: list[int], count_sys: int) -> int:
    new_num = 0

    for i in range(len(num)):
        new_num += num[i] * count_sys ** (len(num) - i - 1)

    return new_num


for n in range(19):
    first = [9, 8, 8, 9, 7, n, 2, 1]
    second = [2, n, 9, 2, 3]

    x = from_some_count_sys(first, 19) + from_some_count_sys(second, 19)
    if x % 18 == 0:
        print(x // 18, n)
