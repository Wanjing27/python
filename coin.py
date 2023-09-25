import time
import random

def coin():
    c=random.randint(0,1)
    if c==1:
        c="heads"
    else:
        c="tales"
    print(c)
    return (c)

class Player:
    def __init__(self,n):
        self.name=n
        self.score=0

    def change_score():
        self.score+=1

def main():
    name=input("what's your name? ")
    player1=Player(name)

main()


