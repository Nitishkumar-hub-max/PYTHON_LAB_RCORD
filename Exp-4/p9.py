pin = input("Enter the 4-digit PIN: ")

if pin == "1234":
    b = float(input("Enter withdrawal amount (₹): "))

    if b <= 10000:
        print("Transaction successfully")
        print("Amount withdrawn: ₹", b)
        print("Available balance: ₹", 10000 - b)
    else:
        print("Insufficient balance")
        print("Total balance you have: ₹", 10000)
else:
    print("Wrong PIN entered.")