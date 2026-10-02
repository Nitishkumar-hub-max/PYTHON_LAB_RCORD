def ev(s, e):
    for i in range(s, e + 1):
        if i % 2 == 0:
            yield i

def od(s, e):
    for j in range(s, e + 1):
        if j % 2 != 0:
            yield j

s = int(input("Enter starting range :"))
e = int(input("Enter ending range :"))
if s > e:
    print("Invalid range")
else:
    print("Even no.s are :")
    for v in ev(s, e):
        print(v, end=" ")
    print()
    print("Odd no.s are :")
    for v in od(s, e):
        print(v, end=" ")