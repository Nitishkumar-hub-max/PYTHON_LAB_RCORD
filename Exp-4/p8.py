dn = int(input("Enter a day no.: "))

if dn < 1 or dn > 7:
    print("Enter a valid day no.")
else:
    if dn == 1:
        print("Monday")
    elif dn == 2:
        print("Tuesday")
    elif dn == 3:
        print("Wednesday")
    elif dn == 4:
        print("Thursday")
    elif dn == 5:
        print("Friday")
    elif dn == 6:
        print("Saturday")
    else:
        print("Sunday")