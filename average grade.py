# Stander Grade
grade=0
# test input & add grads in
for i in range(1,4):
    tgrade=input("Enter the grade for test #"+str(i))
    if tgrade=="a":
        grade=grade+4
    elif tgrade=="b":
        grade=grade+3
    elif tgrade=="c":
        grade=grade+2
    elif tgrade=="d":
        grade=grade+1
    elif tgrade=="f":
        grade=grade+0
    else:
        print ("Error")
# output
print("the average grade for this semester is "+str(grade/3))
