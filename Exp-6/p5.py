def prime(n):
    c = 0
    for i in range(2, n // 2):
        if n % i == 0:
            c = 1
            break
    if c == 1:
        print("It is a prime no.")
    else:
        print("Enter a no:")

n = int(input("Enter a no:"))
prime(n)