a = int(input("Enter 1st no:"))
b = int(input("Enter 2nd no:"))
x, y = a, b
while y != 0: x, y = y, x % y
lcm = (a * b) // x
print("GCD =", x)
print("LCM =", lcm)
