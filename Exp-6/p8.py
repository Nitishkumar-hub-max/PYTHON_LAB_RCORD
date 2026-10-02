a = int(input("Enter 1st no:"))
b = int(input("Enter 2nd no:"))
if a > b: lcm = a
else: lcm = b
while True:
    if lcm % a == 0 and lcm % b == 0: break
    lcm = lcm + 1
print("LCM of 2 no is", lcm)