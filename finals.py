import random

def intro():
    yn=input("Let's play a game called blackjack. Have you played this game before? y or n: ")
    if yn=='y':
        print("Great let's start the game")
    else:
        print("Well here are the rules. The objective of this game is each player attempts to get a count as close to 21 as possible, without going over 21. It is up to each player if an ace is worth 1 or 11. Face cards are 10, and any other card is its pip value.\n The dealer would first give two cards to each player. Then the dealer goes to each player one at a time. The player needs to decide if they want another card (hit) or will sit on what they have as long as you don’t go over 21. \n If you went over 21( which means your busted) or have a lower value then your opponent(who didn't bust), then you lost the game. If both players busted or have the same value, then it is a tied. Which mean if you have cards values thats closer to 21 than your opponent then you win the game.")
        print ("now that you know all the rules, let's start")
    player1=input("Player1, plesae enter your name: ")
    player2=input("Player2, plesae enter your name: ")
    return (player1, player2)

    
def make_deck():
    cardSuits = ["♣","♢","♡","♠"]
    cardRanks = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    deck = []
    values={}
    v=1
    for s in cardSuits:
        for r in cardRanks:
            tempCard = Card(r,s)
            values[tempCard]=bjValue(v)
            deck.append(tempCard)
            v+=1
    return (deck,values)

class Card:
    def __init__(self, r,s):
        self.rank = r
        self.suit = s

    def __str__(self):
        return(self.rank+self.suit)

    def __repr__(self):
        return str(self)
    
def bjValue(card_num):
    rankIndex=card_num%13
    if( rankIndex>=10 or rankIndex==0):
        rankIndex=10
    return (rankIndex)
    
def handout(deck,hand):
    cards=random.choice(deck)
    deck.remove(cards)
    hand.append(cards)
    return(deck,hand)

def ace(value):
    if value==1 or value==11:
        print("there is an ace in your hand, in a value of "+ str(value))
        change=input("want to change the value of the ace? y or n? ")
        while change!='y' and change!='n':
            print("error, try again")
            change=input("want to change the value of the ace? y or n? ")
        if change=='y':
            aces=int(input('what values would it be? 1 or 11? '))
            while aces!=1 and aces!=11:
                print('it an only be 1 or 11, try again')
                aces=int(input('there is an aces in your hand, what values would it be? 1 or 11? '))
            if aces==1:
                value=1
            else:
                value=11
        else:
            print("the value of aces would kept as "+str(value))
    return(value)
    
def findotal(values,hand):
    total=0
    for card in hand:
        value=int(values.get(card))
        value=ace(value)
        total=total+value
    print("the total now is "+str(total))
    return total

def mid_game(dealhand,hand_deck,total,values,game):
    i=0
    while i <= 5:
        decision=input("Do you want to [H]it: get another card or [S]tand: hold: ").lower()
        while (decision!='h')and(decision!='s'):
            print(" just enter the first letter of the options, for example if you want to hit, enter h")
            decision=input("Do you want to [H]it: get another card, [S]tand: hold, or [Q]uit: ").lower()
        if decision=='h':
            (dealhand,hand_deck)=handout(dealhand,hand_deck)
            print (*hand_deck, sep = ", ")
            total=findotal(values,hand_deck)
            (i,total)=check(total,i)
        elif decision=='s':
            print('okay')
            i=7
    game+=1
    return(dealhand,hand_deck,total,game)

def check(total,i):
    if total==21:
        print("Congratulations! You got a Blackjack!")
        i=7
    elif total>21:
        print("OH NO, BUSTED\nbetter luck next time")
        i=7
        total=0
    else:
        i=i+1
    return(i,total)

def setPlayer(player1, player2,game):  #get player
    if game%2!=0:
        player=player2
    else:
        player=player1
    return player
def setGame():
    (player1, player2)=intro()
    (dealhand,values)=make_deck()
    hand_deck=[]
    total=0
    game=0
    player_list={}
    return(player1, player2,dealhand,values,hand_deck,total,game,player_list)

def wholeGame(player1, player2,dealhand,values,hand_deck,total,game,player_list):
    while game<=1:
        hand_deck=[]
        player=setPlayer(player1, player2,game)
        print(player+" here is your cards")
        for i in range(2):
            (dealhand,hand_deck)=handout(dealhand,hand_deck)
        print (*hand_deck, sep = ", ")
        total=findotal(values,hand_deck)
        (dealhand,hand_deck,total,game)=mid_game(dealhand,hand_deck,total,values,game)
        player_list[player]=total
    return(player_list)

        
def main():
    (player1, player2,dealhand,values,hand_deck,total,game,player_list)=setGame()
    player_list= wholeGame(player1, player2,dealhand,values,hand_deck,total,game,player_list)
    player_value(player1, player2,player_list)

def player_value(player1, player2,player_list):
    print(player_list)
    player1_value=(player_list.get(player1))
    player2_value=(player_list.get(player2))
    if player1_value==player2_value:
        print("tie, both player have the same values")
    elif player1_value < player2_value:
        print(player1+" Congration you won")
    elif player1_value > player2_value:
        print(player2+" Congration you won")
    
main()
