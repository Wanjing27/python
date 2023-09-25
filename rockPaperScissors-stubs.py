#based on C5B21.py solution by Angela Koshida
import random

def main():
    intro()
    kG="y"
    while kG=="y":
        playGame()
        kG=input("Would you like to play again? [y/n]")
        
    print("thanks for playing!")

def playGame():
    #INPUT: none
    #PROCESS: play game
    #OUTPUT: none (reports game state) 
    p=playerChoice()
    c="s"#computerChoice()
    print("Your AI opponent chose", convert2word(c))

    findWinner(p,c)
    
def intro():
    #INPUT: none
    #PROCESS: print out guide for the game
    #OUTPUT: none
    print("need to write")
    
def playerChoice():
    #INPUT: none
    #PROCESS: ask client for choice (r:rock, p:paper, s:scissors)
    #OUTPUT: return choice of r, s or p
    ch="r"  #STUB: just r for now; 
    return ch

def convert2word(choice):
    #INPUT: game move/choice encoded as a single letter
    #PROCESS: convert r:rock, s:scissors p:paper
    #OUTPUT: full word game move

    fullWord = "rock"  #STUB: rock for now
    return(fullWord)

def computerChoice():
    #INPUT: none
    #PROCESS: pick a random number and associate it with r, p or s
    #OUTPUT: r,s or p 
    ch = "s"  #STUB:just s for now
    return ch


def findWinner(p,c):
    #INPUT: p is the player's choice
           #c is the computer's choice
    #PROCESS: find out if your client, the player, wins or loses and report answer
    #OUTPUT: none
    youLose(p,c)        # will return True if client loses; False otherwise
    reportResult(p,c)   #report result if not a tie


def youLose(p,c):
    #INPUT: p is the player's choice
           #c is the computer's choice
    #PROCESS: find out if your client wins or loses
    #OUTPUT: True or False
    
    return(True)    #Stub: True for now
    
def reportResult(c1,c2):
    #INPUT: 2 choices (player and computer, order doesn't matter)
    #PROCESS: reports common phrase like "Rock smashes scissors"
    #OUTPUT: none
    print("STUB: needs to be written")
 
