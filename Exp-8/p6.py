numbers = [10, 20, 30, 40, 50]

target = int(input("Enter target sum: "))

print("Pairs whose sum is:", target, "--")

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(numbers[i], numbers[j])