n = int(input("Enter no- of rows:"))
while True:
    print("==== STAR MENU ====")
    print("1. Square star pattern")
    print("2. Right angled star pattern")
    print("3. Inverted right angled star pattern")
    print("4. Right alligned right angle star pattern")
    print("5. Inverted right alligned right angle star pattern")
    print("6. EXIT")
    c = int(input("Enter your choice:"))
    match c:
        case 1:
            for i in range(n): print("*" * n)
        case 2:
            for i in range(1, n+1): print("*" * i)
        case 3:
            for i in range(n, 0, -1): print("*" * i)
        case 4:
            for i in range(1, n+1):
                print(" " * (n - i), "*" * i)
        case 5:
            for i in range(1, n+1):
                print(" " * (i - 1), "*" * (n - i + 1))
        case 6:
            break
        case _:
            print("Invalid choice")