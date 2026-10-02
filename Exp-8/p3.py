numbers = [0,10,5,0,20,0,15,30]

result = []

for x in numbers:
    if x != 0:
        result.append(x)

for x in numbers:
    if x == 0:
        result.append(x)

print("original list:", numbers)
print("list after moving zeros:", result)