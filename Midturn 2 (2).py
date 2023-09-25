# intro
def intro():
    answer=input(" Have your ever played the game call: hangeman? y or n: ")
    if answer=='y':
        print("Well this the same thing, but we are builing a snowman this time.")
    else:
        print("Well here is something fun for you to play. This game is called Snowman, we pick a secret word for you, the player, to guess. Each player has a chance to guess one letter, that contained in the secret word, at a time. When the guesses are correct, the correction will appear on the blank where it occurs. However, when the guesses are wrong, the player would earn a strike that brings them closer to losing, to show this, adding a new part to the snowman with every wrong answer, when a snowman full appeared that mean game over. The player wins the game by correctly guessing the full word before the snowman fully appears.")
        print ("now that you know all the rules, let's start")
    player1=input("Player1, plesae enter your name: ")
    player2=input("Player2, plesae enter your name: ")
    return (player1, player2)

# setup for games
def word():  #pick words
    words_list=[]
    file=open("hangman.txt","r")
    lines = file.readlines()
    file.close()
    for line in lines:
        line = line.strip().upper()
        words_list.append(line)
    import random
    word=random.choice(words_list)
    secretWord=list(word)
    sword_list={}
    x=0
    for letter in secretWord:
        sword_list.update({x:letter})
        x+=1
    return (secretWord,sword_list)

def display_word(word):  #showed word
    display=[]
    display+=len(word)*[' _ ']
    print("secret word: "+' '.join(display))
    return display

def player(player1, player2,game):  #get player
    if game%2!=0:
        player=player1
    else:
        player=player2
    return player

#grid
def printPretty(g):
    rows = len(g)
    cols = len(g[0])
    for r in range(rows):
        for c in range (cols):
            print(g[r][c],end="")
        print()

def change_grid(x,y,z,grid):
    grid[x][y]=z
        
def snow_man(wrong):
    grid = [[' ',' ',' '],
            [' ',' ',' '],
            [' ',' ',' '],
            ['-','-','-']]
    wrong_dic={0:[2,1,'o'],1:[1,1,'o'],2:[0,1,'o'],3:[1,0,'/'],4:[1,2,'\\']}
    wronglist=[]
    for i in range(wrong):
        (rows, cols,symbols)=wrong_dic[i]
        change_grid(rows, cols,symbols,grid)
    printPretty(grid)

# Set up
def startgame_setting():
    bad_guesses=[]
    wrongGuess=0
    correct_guesses=0
    (secret_word,sword_list)=word()
    display=display_word(secret_word)
    game=0
    return(bad_guesses,wrongGuess,correct_guesses,secret_word,sword_list,display,game)
    
# process of game
def guess_word(secret_word, player,wrong):
    answer=input(player+" want to guess the word ? y/n ").lower()
    while answer!='y' and answer!='n':
        print("error, try again")
        answer=input(player+" want to guess the word ? y/n ").lower()
    if answer=="y":
        gword=list(input("what is the secret word: ").upper())
        if gword==secret_word:
            print(" Correct!! Congrats "+ player+ " you won the game!!")
            wrong=6
        else:
            print( "noo... better luck next time")
    elif answer=="n":
        print("maybe wait until you got more info")
    return(wrong)

def getAlphabet():
    alphabet=[]
    for i in range (65,91):
        letter=chr(i)
        alphabet.append(letter)
    return(alphabet)

def letter(letter, player):
    alphabet=getAlphabet()
    while letter not in alphabet:
        print("error, this is not a letter. Try again")
        letter=input(player+": what letter would be in this secret word? ")
    return letter

def gletter(player,bad_guesses):
    word=input(player+": what letter would be in this secret word? ").upper()
    word=letter(word,player)
    word=repet_letter(word,bad_guesses)
    return (word)


def check_game(correct, secret_word):
    if correct==len(secret_word):
        print("game over")
        game=False
    else:
        game=True
    return game

def check_letter(letter,secret_word,display,correct,bad, wrong,sword_list,game):
    if letter in secret_word:
        print("right")
        correct+=1
        for x in range(len(secret_word)):
            if sword_list[x]==letter:
                display[x]=letter
    else:
        print("wrong")
        bad.append(letter)
        wrong+=1
        game=game+1
    print("wrong guesses: ",bad)
    print("secret word: "+' '.join(display))
    return (correct,bad,wrong,game)

def repet_letter(letter, bad):
    while letter in bad:
        letter=input(letter+" Had already been guessed. Guess again:").upper()
        print(bad)
        
    return(letter)

# the game
def gameplay(player1, player2):
    (bad_guesses,wrongGuess,correct_guesses,secret_word,sword_list,display,game)=startgame_setting()
    while wrongGuess<=4:
        curret_player=player(player1, player2,game)
        guessLetter=gletter(curret_player,bad_guesses)
        (correct_guesses,bad_guesses,wrongGuess,game)=check_letter(guessLetter,secret_word,display,correct_guesses,bad_guesses,wrongGuess,sword_list,game)
        snow_man(wrongGuess)
        if check_game(correct_guesses,secret_word)==False:
            print(" Correct!! Congrats ", player, "you won the game!!")
            wrongGuess+=7
        wrongGuess=guess_word(secret_word,curret_player,wrongGuess)
        if wrongGuess==5 and check_game(correct_guesses,secret_word):
            print("tied game, on one wins")
            print ("the secret is ",secret_word)

# Ask the player if they want to play again
def endgame(x):
    answer=input("another round? y/n: ")
    while answer!='y' and answer!='n':
        print("error, try again")
        answer=input("another round? y/n: ")
    if answer=="y":
        x=0
    else:
        print("Game Over")
        x=2
    return x


def main():
    (player1, player2)=intro()
    x=0
    while x<1:
        gameplay(player1, player2)
        x=endgame(x)

main()


    


