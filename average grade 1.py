grade=0
test=1
while test< 4:
    tgrade=input("Enter the grade for test #"+str(test))
    if tgrade=="a":
        grade=grade+4
        test=test+1
    elif tgrade=="b":
        grade=grade+3
        test=test+1
    elif tgrade=="c":
        grade=grade+2
        test=test+1
    elif tgrade=="d":
        grade=grade+1
        test=test+1
    elif tgrade=="f":
        grade=grade+0
        test=test+1
    else:
        print ("Error.. try again")
print("the average grade for this semester is "+str(grade/3))
