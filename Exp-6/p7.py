n = int(input("Enter a no"))
for d in range(10):
    t, c = n, 0
    while t > 0:
        r = t % 10
        if d == r: c = c + 1
        t = t // 10
    if c > 0: print(d, "occares", c, "time")