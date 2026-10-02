print("==== Scientific Calculator ====")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Square")
print("6. Cube")
print("7. Square root")
print("8. Power")
c = int(input("Enter your choice :"))
match c:
    case 1:
        a = float(input("Enter 1st no:"))
        b = float(input("Enter 2nd no:"))
        print("Result= ", a+b)
    case 2:
        a = float(input("Enter 1st no:"))
        b = float(input("Enter 2nd no:"))
        print("Result= ", a-b)
    case 3:
        a = float(input("Enter 1st no:"))
        b = float(input("Enter 2nd no:"))
        print("Result= ", a*b)
    case 4:
        a = float(input("Enter numerator"))
        b = float(input("Enter denominator:"))
        if b!=0: print("Result= ", a/b)
        else: print("Denominator can't be zero.")
    case 5:
        a = float(input("Enter a no:"))
        print("Result= ", a**2)
    case 6:
        a = float(input("Enter a no:"))
        print("Result= ", a**3)
    case 7:
        a = float(input("Enter a no:"))
        print("Result= ", a**0.5)
    case 8:
        a = float(input("Enter base no:"))
        b = float(input("Enter power:"))
        print("Result= ", a**b)
    case _: print("Invalid choice.")