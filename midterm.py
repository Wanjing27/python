# defind values
import random
answer= random. randint(0,10)
i=0
x=1
win=0

# Set up functions
def test_guess(gnumber):
    if gnumber > 10 or gnumber< 1:
        print("out of range, try again")
     elif gnumber == answer:
         print("correct, congratulations "+ player +", you have won the game")
         i=i+7
         print(other+" you lose, thanks for trying")
    elif gnumber < answer or gnumber > answer:
        i=i+1
        if gnumber < answer:
            print("Wrong, it is too small")
        else:
            print("nope, it is too big")
    return(i)

def keep_going:
    keepgoing=input(" want to play again? y/n: ")
        if keepgoing=="y":
            i=0
            print(" New Game")
            answer= random. randint(0,10)
        else:
            print("game over")
    return(i)

def players(x):
    if x%2==0:
        player=player2
        other=player1
    else:
        player=player1
        other=player2
#rules
print("Welcome to the Number Guessing Game\nThe goal of this game is to guess a number between 1 and 10.\neach player have 3 chances to guess the number.\nwho ever got it right first won the game.")
player1=input("player 1: enter your name: ")
player2=input("player 2: enter your name: ")
print ("let's get started")


#start game
for y in [3]:
    player=players(x)
    gnumber=int(input(player +" what is your guess: "))
    
