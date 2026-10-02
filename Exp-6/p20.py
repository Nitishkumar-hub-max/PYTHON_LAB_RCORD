def valid(fun):
    def wrap(a):
        if a <= 0:
            print("Invalid amount")
            return
        return fun(a)
    return wrap

def tran(fun):
    def wrap(a):
        res = fun(a)
        print("Transaction completed")
        return res
    return wrap

@tran
@valid
def am(a):
    print("Deposited :", a)

a = int(input("Enter amount:"))
am(a)