numbers = [1,2,3,4,5,6,3,4,5,6]

dublicates = []
unique = []

for x in numbers:

    if numbers.count(x) > 1:
        if x not in dublicates:
            dublicates.append(x)

    else:
        unique.append(x)

print("duplicate elements:", dublicates)
print("unique elements:", unique)