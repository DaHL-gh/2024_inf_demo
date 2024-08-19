func = lambda x, y, z, w: (x and not y) or (y == z) and not w

rng = range(0, 2)
truth_table = []
for x in rng:
    for y in rng:
        for z in rng:
            for w in rng:
                print(x, y, z, w, func(x, y, z, w))
