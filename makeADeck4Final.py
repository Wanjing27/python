import random
class Card:
    def __init__(self, r,s):
        self.rank = r
        self.suit = s

    def __str__(self):
        return(self.rank+self.suit)

    
def main():
    deck = makeADeck()
    for card in deck:
        print(card)

def makeADeck():
    cardSuits = ["♣","♢","♡","♠"]
    cardRanks = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    deck = []
    for s in cardSuits:
        for r in cardRanks:
            tempCard = Card(r,s)
            deck.append(tempCard)
    
#    random.shuffle(deck)
    return(deck)

main()
