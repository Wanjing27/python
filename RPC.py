# rock, paper, scissors
import random

def computer_play():
    play=random.randint(0,2)
    if play==0:
        cp="rock"
    elif play==1:
        cp="paper"
    elif play==2:
        cp="scissors"
    return cp

def player_play():
    pp=input(" rock! paper!scissors! shoot!(enter what your going to play)").lower()
    while pp!="rock" and pp!="paper" and pp!="scissors":
        print("error try again")
        pp=input(" what are you going to play? rock? paper? or scissors?").lower()
    return pp

def result(pp,cp):
    if cp=="rock":
        if pp=="rock":
            print("tie, play again")
        elif pp=="paper":
            print( "you won")
        else:
            print("you lost")
    elif cp=="paper":
        if pp=="paper":
            print("tie, play again")
        elif pp=="scissors":
            print( "you won")
        else:
            print("you lost")
    else:
        if pp=="scissors":
            print("tie, play again")
        elif pp=="rock":
            print( "you won")
        else:
            print("you lost")

def main():
    print ("let's pay a game of rock, paper,and scissor")
    i=0
    while i<5:
        print( "ready?")
        cp=computer_play()
        pp=player_play()
        print(cp)
        result(pp,cp)
        i=again(i)
        
    print("gmae over")

def again():
    again=input("want to play again? y/n ").lower()
        while again!="n" and again!="y":
            print("error, try again")
        if again=="y":
            print("okay")
            i=i+1
        else:
            print("cool")
            i=i+6
        return i

main()

