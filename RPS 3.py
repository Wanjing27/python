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
    if c==P:
        print("tie, play again")
    else:
        reportResult(p,c)
        if youLose(p,c):
            print(" you lose")
        else:
            print(" you won")
