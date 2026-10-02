def fibonacci(n,a=0,b=1):
    if n==0:
        return 1
    else:
        print("a",end="")
        fibonacci(n-1,b,a+b)
num=int(int(input("enter the number:")))
fibonacci(num)
