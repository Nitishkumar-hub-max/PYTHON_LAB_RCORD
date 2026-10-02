def harshad(n):
    r, t = 0, n
    while n > 0:
        temp = n % 10
        r = r + temp
        n = n // 10
    if t % r == 0:
        print("It is a harshad no.")
    else:
        print("It is not a harshad no.")

n = int(input("Enter a no:"))
harshad(n)