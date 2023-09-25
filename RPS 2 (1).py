import random
def computeChoice():
    play=random.randint(0,2)
    if play==0:
        ch="r"
    elif play==1:
        ch="p"
    elif play==2:
        ch="s"
    return ch

def findWinner(p,c):
    if c=="r":
        if p=="r":
            print("tie, play again")
        else:
            reportResult(p,c)
            if youLose(p,c)=="True":
                print(" you lose")
            else:
                print(" you won")
    elif c=="p":
        if p=="p":
            print("tie, play again")
        else:
            reportResult(p,c)
            if youLose(p,c)=="True":
                print(" you lose")
            else:
                print(" you won")
    else:
        if p=="s":
            print("tie, play again")
        else:
            reportResult(p,c)
            if youLose(p,c)=="True":
                print(" you lose")
            else:
                print(" you won")
