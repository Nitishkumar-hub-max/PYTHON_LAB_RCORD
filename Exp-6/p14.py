def grade(gr):
    if gr == "O":
        return 10
    elif gr == "E":
        return 9
    elif gr == "A":
        return 8
    elif gr == "B":
        return 7
    elif gr == "C":
        return 6
    elif gr == "D":
        return 5
    else:
        return 0

def cal(*sc):
    return sum(sc)

def calcgpa(tot):
    return tot / 6

gr = ("A", "O", "A", "B", "D")
s = calcgpa(cal(*(grade(i) for i in gr)))
print(f"SGPA = {s:.2f}")