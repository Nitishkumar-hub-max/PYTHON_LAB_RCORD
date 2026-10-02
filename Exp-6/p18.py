def auto(fun):
    def wrap(un, pas):
        if un == "admin" and pas == "1234":
            return fun(un, pas)
        print("Invalid username and password")
    return wrap

@auto
def access(u, p):
    print("Welcome", u)
    print("Access Granted")

u = input("Enter username :")
p = input("Enter password :")
access(u, p)