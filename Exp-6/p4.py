n = int(input("Enter the range :"))
for i in range(1, n+1):
    if i % 2 != 0: continue
    print(i, end=" ")
print("odd no.s are:")
for i in range(1, n+1):
    if i % 2 == 0: continue
    print(i, end=" ")