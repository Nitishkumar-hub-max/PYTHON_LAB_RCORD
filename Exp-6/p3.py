s = int(input("Enter starting no:"))
e = int(input("Enter ending no:"))
for i in range(s, e):
    if i % 5 != 0 and i % 7 == 0 and i % 11 == 0:
        print(i, "divisible by 7 and 11 but not divisible by 5")
        break