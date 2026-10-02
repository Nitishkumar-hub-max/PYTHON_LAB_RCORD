s = input("Enter a string: ")

upper = sum(ch.isupper() for ch in s)
lower = sum(ch.islower() for ch in s)
digit = sum(ch.isdigit() for ch in s)

special = len(s) - upper - lower - digit

print("Uppercase:", upper)
print("Lowercase:", lower)
print("Digits:", digit)
print("Special characters:", special)