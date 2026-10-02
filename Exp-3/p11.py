s = input("Enter a string: ")

print("Alternate characters:", s[::2])
print("Odd position characters:", s[0::2])
print("Every third character:", s[::3])
print("Remove first character:", s[1:])
print("Remove last character:", s[:-1])