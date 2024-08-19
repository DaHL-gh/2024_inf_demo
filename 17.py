file = open("17.txt")

max_n = 0
for num in file:
    num = int(num)

    if num % 100 == 13 and num > max_n:
        max_n = num

print(max_n)

file.seek(0)

max_s = 0
c = 0
f = int(file.readline())
s = int(file.readline())
for num in file:
    t = int(num)

    num_sum = f + s + t

    if not(num_sum > max_n) and sum(1 if x // 1000 == 0 else 0 for x in (f, s, t)):
        if num_sum + max_s:
            max_s = num_sum
        c += 1

print(c, max_s)