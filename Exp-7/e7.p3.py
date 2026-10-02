def sum(n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)
     
        
num=int(int(input("enter the number:")))
print(sum(num))
