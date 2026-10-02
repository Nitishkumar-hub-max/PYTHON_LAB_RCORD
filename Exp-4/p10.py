unit = float(input("Enter units: "))
bill = 0

if unit <= 50:
    bill = unit * 2.5

elif unit <= 150:
    bill = 50 * 2.5 + (unit - 50) * 3.5

elif unit <= 250:
    bill = 50 * 2.5 + 100 * 3.5 + (unit - 150) * 4.2

else:
    bill = 50 * 2.5 + 100 * 3.5 + 100 * 4.2 + (unit - 250) * 5.5

print("Electricity bill = ₹", bill + (bill * 20 / 100))