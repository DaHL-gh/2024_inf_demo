for A in range(10000):
    c1 = 0
    c2 = 0
    for x in range(70):
        for y in range(70):
            if (x + 2*y < A) or (y > x) or (x > 60):
                c1 += 1
            c2 += 1

    if c1 == c2:
        print(A)
        break