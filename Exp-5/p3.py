a = int(input("Enter the amount: "))
if a >= 500:
    n = a // 500
    print("No. of 500 notes:", n)
    a = a % 500
if a >= 200:
    n = a // 200
    print("No. of 200 notes:", n)
    a = a % 200
if a >= 100:
    n = a // 100
    print("No. of 100 notes:", n)
    a = a % 100
if a >= 50:
    n = a // 50
    print("No. of 50 notes:", n)
    a = a % 50
if a >= 20:
    n = a // 20
    print("No. of 20 notes:", n)
    a = a % 20
if a >= 10:
    n = a // 10
    print("No. of 10 notes:", n)
    a = a % 10
if a >= 5:
    n = a // 5
    print("No. of 5 notes:", n)
    a = a % 5
if a >= 2:
    n = a // 2
    print("No. of 2 notes:", n)
    a = a % 2
if a >= 1:
    n = a // 1
    print("No. of 1 notes:", n)