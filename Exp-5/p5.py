c = input("Enter traffic light colour:")
s = c.lower()
match s:
    case "red" : print("STOP")
    case "yellow": print("READY TO GO")
    case "green": print("GO AHEAD")
    case _ : print("Invalid signal Colour/light")