n1 = int(input("Enter 1st no.: "))
n2 = int(input("Enter 2nd no.: "))
n3 = int(input("Enter 3rd no.: "))

if n1 > n2:
    if n1 > n3:
        print("Largest no. is:", n1)
    else:
        print("Largest no. is:", n3)
else:
    if n2 > n3:
        print("Largest no. is:", n2)
    else:
        print("Largest no. is:", n3)