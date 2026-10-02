a=1
b=3
def add(a,b):
    if b==0:
        return a
    
    return add(a+1,b-1)
print("add=",add(a,b))