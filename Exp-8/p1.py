# 1. Using square brackets
list1 = [10, 20, 30, 40, 50]
print("1. Using square brackets:", list1)


# 2. Taking elements from user
list2 = []
n = int(input("Enter number of elements: "))
for i in range(n):
    element = int(input())
    list2.append(element)

print("2. List:", list2)


# 3. Using list constructor
list3 = list((10, 20, 30, 40))
print("3. Using list constructor:", list3)


# 4. Using range()
list4 = list(range(1, 6))
print("4. Using range():", list4)


# 5. Using enumerate()
print("\n5. Using enumerate():")

for index, value in enumerate(list4):
    print("Index", index, "=", value)


# 6. Using while loop
print("\n6. Using while loop:")

i = 0
while i < len(list4):
    print(list4[i], end=" ")
    i = i + 1


# 7. Taking multiple elements in one line
numbers = list(
    map(int, input("\nEnter the elements separated by space: ").split())
)

print("7. List:", numbers)