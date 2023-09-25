color1=str(input(" what is the the first color? ").lower())
color2=str(input("what is the second color? ").lower())
if color1 == "red":
    if color2== "blue":
        print(" purple")
    elif color2=="yellow":
        print(" orange")
    elif color2=="red":
        print(" still red")
    else:
        print("nah")
if color1=="blue":
    if color2== "red":
        print(" purple")
    elif color2=="yellow":
        print(" green")
    elif color2=="blue":
        print(" still yellow")
    else:
        print("nah")
if color1=="yellow":
    if color2== "blue":
        print(" green")
    elif color2=="yellow":
        print(" still yellow")
    elif color2=="red":
        print("orange")
    else:
        print("undefind")
else:
    print(" undefind")
