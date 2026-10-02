ch = input("Enter a character: ")

if ch.isdigit():
    print(ch, "is a digit")
elif ch.isalpha():
    if ch in "AEIOUaeiou":
        print(ch, "is a vowel")
    else:
        print(ch, "is a consonant")
else:
    print(ch, "is a special character")