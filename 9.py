file = open("9_2024.csv")

c = 0
for line in file:
    nums = list(map(int, line.replace("\n", "").split(";")))
    counts = [nums.count(x) for x in nums]
    if sum(counts) == 11:
        rep = non_rep = 0
        for i in range(7):
            if counts[i] == 2:
                rep += nums[i]
            else:
                non_rep += nums[i]

        if rep / 4 < non_rep / 3:
            c += 1

print(c)