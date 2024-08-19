c = 0

for i1 in range(1, 8):
    for i2 in range(8):
        for i3 in range(8):
            for i4 in range(8):
                for i5 in range(8):
                    nums = [i1, i2, i3, i4, i5]
                    if any(x == 1 for x in nums):
                        pass
                    elif any((nums[i] == nums[j]) and (j != i)for i in range(5) for j in range(5)):
                        pass
                    elif all(nums[i] % 2 != nums[i + 1] % 2 for i in range(4)):
                        c += 1

print(c)