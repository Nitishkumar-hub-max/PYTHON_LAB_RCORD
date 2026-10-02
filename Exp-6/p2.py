while True:
    print("==== Menu Driven Program ====")
    print("1. Count the no of digits.")
    print("2. Sum of digits.")
    print("3. Product of digits.")
    print("4. Reverse the no:")
    print("5. Check for palindrome no.")
    print("6. Check for armstrong no:")
    print("7. Check for strong no:")
    print("8. Check for perfect no:")
    print("9. Exit the program")
    ch = int(input("Enter your choice:"))
    match ch:
        case 1:
            n = int(input("Enter a no:"))
            c = 0
            while n > 0:
                c = c + 1
                n = n // 10
            print("Result = ", c)
        case 2:
            n = int(input("Enter a no:"))
            s = 0
            while n > 0:
                t = n % 10
                s = s + t
                n = n // 10
            print("Result = ", s)
        case 3:
            n = int(input("Enter a no:"))
            p = 1
            while n > 0:
                t = n % 10
                p = p * t
                n = n // 10
            print("Result = ", p)
        case 4:
            n = int(input("Enter a no"))
            r = 0
            while n > 0:
                t = n % 10
                r = r * 10 + t
                n = n // 10
            print("Result = ", r)
        case 5:
            n = int(input("Enter a no:"))
            r = 0
            d = n
            while n > 0:
                t = n % 10
                r = r * 10 + t
                n = n // 10
            if d == r: print("It is a palindrome no:")
            else: print("It is not a palindrome no:")
        case 6:
            n = int(input("Enter a no:"))
            s = 0
            d = n
            p = len(str(n))
            while n > 0:
                t = n % 10
                s = s + t ** p
                n = n // 10
            if d == s: print("It is a armstrong no.")
            else: print("It is not a armstrong no.")
        case 7:
            n = int(input("Enter a no:"))
            s = 0
            d = n
            while n > 0:
                t = n % 10
                f = 1
                for i in range(1, t+1):
                    f = f * i
                s = s + f
                n = n // 10
            if d == s: print("It is a strong no")
            else: print("It is not strong no")
        case 8:
            n = int(input("Enter a no:"))
            s = 0
            d = n
            for i in range(1, n):
                if n % i == 0:
                    s = s + i
            if d == s: print("It is a perfect no")
            else: print("It is not a perfect no")
        case 9:
            print("EXIT")
            break
        case _:
            print("Invalid choice")
