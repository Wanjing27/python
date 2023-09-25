class Card():
    suits=["diamond","club","heart","spade"]
    def __init__(self,r,s):
        self.rank=r
        self.suit=s

    def setValues(self):
        dvalues={'1':'A',11:'J',12:'Q',13:'K'}
        for key in dvalues:
            if self.rank == key:
                print(dvalues[key])
                self.rank=dvalues[self.rank]

    def __str__(self):
        return(self.rank+' of '+self.suit)
    def __repr__(self):
        return str(self)

def cards():
    rank=input("pick a number: ")
    suits=["diamond","club","heart","spade"]
    suit=input("pick a suit: ").lower()
    card_info=Card(rank,suit)
    card_info.setValues()
    return card_info

def compare(secret, guess):
    if secret.rank > guess.rank:
        ("number is too big")
    elif  secret.rank <guess.rank:
        ("number is too small")
    else:
        ("correct number")
    if secret.suit != guess.suit:
        print("wrong suit")

def main():
    print("Hey guess my card")
    secret=Card("12","heart")
    guess=cards()
    compare(secret, guess)

main()
