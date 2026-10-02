print("==== ATM Banking System ====")
p = input("Enter pin:")
if p == "1234":
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    c = input("Enter your choice:")
    match c:
        case "1":
            print("Balance you have : Rs. 500000")
        case "2":
            d = int(input("Enter deposit amount:"))
            print("Amount deposited successfully.")
            print("Balance you have: Rs. ", 500000+d)
        case "3":
            w = int(input("Enter withdrawal amount:"))
            if w > 500000:
                print("Insufficient balance.")
                print("Balance you have : Rs 500000")
            else:
                print("Amount withdrawal successfully.")
                print("Amount you withdraw : Rs ,", w)
                print("Balance you have : Rs ", 500000-w)
        case _:
            print("Invalid choice.")
else: print("Wrong ATM pin.")