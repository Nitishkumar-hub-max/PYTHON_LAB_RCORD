n = int(input("Enter the range :"))
a = 0
b = 1
print("The Fibonacci series is:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b