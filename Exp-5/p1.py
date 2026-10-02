a1 = float(input("Enter 1st angle: "))
a2 = float(input("Enter 2nd angle: "))
a3 = float(input("Enter 3rd angle: "))
a = a1 + a2 + a3
if a1 <= 0 or a2 <= 0 or a3 <= 0:
    print("Invalid triangle")
elif a == 180:
    print("Valid triangle")
else:
    print("Invalid triangle")