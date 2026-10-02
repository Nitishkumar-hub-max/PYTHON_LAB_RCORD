def spy(n):
    s, p = 0, 1
    while n > 0:
        t = n % 10
        s = s + t
        p = p * t
        n = n // 10
    if s == p:
        print("It is a spy no")
    else:
        print("It is not a spy no.")

n = int(input("Enter a no:"))
spy(n)