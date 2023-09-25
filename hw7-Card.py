
class Card:
    
    def __init__(self, r, s):
        self.suit = s
        self.rank = r

    def __str__(self):
        return(self.rank + self.suit )


def main():
    print("Demos instantiation of 2 Card objects from the same Card class")
    print("Includes a __str__ method to print out information") 
    #1. make a Card
    #1. get all the info you need to make the Card
 

    #2. use the constructor (__init__() ) to make the Card
    #   aka instantiate a Card object using the Card class
    card1 = Card("7","♠")
    # again for a second card
    card2 = Card("Q","♡")

    collection = []
    collection.append(card1)
    collection.append(card2)
    
    #prettier print bc of __str__
    for card in collection: 
        print(card, end="      ")


main()    
