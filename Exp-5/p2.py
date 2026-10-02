s1 = float(input("Enter 1st side: "))
s2 = float(input("Enter 2nd side: "))
s3 = float(input("Enter 3rd side: "))
if s1+s2>s3 and s1+s3>s2 and s2+s3>s1:
    if s1 == s2 or s2 == s3 or s1 == s3:
        print("It is an isosceles triangle")
    else:
        print("It is a scalene triangle")
else:
    print("It is not a valid triangle")