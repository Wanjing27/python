#rules
print("Welcome to the Number Guessing Game\nThe goal of this game is to guess a number between 1 and 10.\nThere would be three rounds of the match.\nEach round every player would have three chances to guess the number.\nWhoever guess the number right first win the round, and whoever earned the most rounds win the game.")
player1=input("player 1: enter your name: ")
player2=input("player 2: enter your name: ")

# set values
import random
turns=0
x=1
win=0
games=0
gameplay=0
score1=0
score2=0

#start game
print ("start game")
while games<3:
    answer= random. randint(1,10)
    turns=0
    while turns < 6:
# set up player
        if x%2==0:
            player=player2
            other=player1
        else:
            player=player1
            other=player2
        if turns>3:
            print( player + " this is your last chanes")
# test number
        gnumber=int(input(player +" what is your guess: "))
        if gnumber > 10 or gnumber< 1:
            print("out of range, try again")
        elif gnumber == answer:
            print("correct, congratulations "+ player +", you have won this round")
            turns=turns+7
            games=games+1
            gameplay=gameplay+1
            if x%2==0:
                score2=score2+1
            else:
                score1=score1+1
            print(other+" you lose, thanks for trying")
            if games==3:
                print(" Game )ver")
            else:
                keepgoing=input(" want to play again? y/n: ")
                if keepgoing=="y":
                    print(" New Game")
                else:
                    games=4
                    print("game over")
        elif gnumber < answer or gnumber > answer:
            turns=turns+1
            x=x+1
            if gnumber < answer:
                print("Wrong, it is too small")
            else:
                print("nope, it is too big")
# out of chances
        if turns==6:
            print( " out of chances, the answer is " +str(answer))
            print("both of you have lost this round, thanks for trying")
            gameplay=gameplay+1
            if games==3:
                ptinr(" game over")
            else:
                keepgoing=input(" want to play again? y/n: ")
                if keepgoing=="y":
                    print(" New Game")
                else:
                    games=4
                    print("game over")

#end of the Game
if score2>score1:
    print("congratulations "+ player2 +", you have won the game with the score of "+str( score2)+"/"+str(gameplay))
else:
     print("congratulations "+ player1 +", you have won the game with the score of "+str( score1)+"/"+str(gameplay))
