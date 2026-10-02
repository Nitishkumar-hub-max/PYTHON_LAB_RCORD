def square(a, b):
    for i in range(a, b + 1):
        if i % 3 == 0:
            print(i, "=", i ** 2)

x = int(input("Enter starting range :"))
y = int(input("Enter ending range :"))
square(x, y)