def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
a=int(input("enter the first number:"))
b=int(input("enter the second number;"))
print("gcd=",gcd(a,b))
    