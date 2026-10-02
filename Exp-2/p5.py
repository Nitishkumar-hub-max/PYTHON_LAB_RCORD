n = int(input("Enter a three-digit number: "))

a = n // 100
b = (n // 10) % 10
c = n % 10

print("Sum =", a + b + c)