for n in range(0, 10**10, 2024):
    sn = str(n)
    if sn[:1] == "1" and sn[2:6] == '2157' and sn[-1] == "4":
        print(n, n//2024)