numbers = [10, 5, 22, 7, 15, 54, 14, 22]

largest = second_largest = numbers[0]

for num in numbers:

    if num > largest:
        second_largest = largest
        largest = num

    elif num != largest and num > second_largest:
        second_largest = num

print("Largest =", largest)
print("2nd largest =", second_largest)