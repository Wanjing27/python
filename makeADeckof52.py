import random
def makeADeckOf52():
    #input: none
    #output: a list of 52 numbers (1-52, inclusive) in random order
    #process: randomly generate 52 numbers with no duplicates
    #debug: deal a smaller deck by making NUM_OF_CARDS_IN_DECK smaller
    NUM_OF_CARDS_IN_DECK=52
    deck = []
    #LCV: the length of the deck
    for i in range (1,NUM_OF_CARDS_IN_DECK+1):
        deck.append(i)
    random.shuffle(deck)
    
    ### you can comment out the next three print lines after you run this once   
    print(deck)          # just to make sure deck got made
    print()
    print(sorted(deck))  #easier to check if all cards are in the deck
    return(deck)

makeADeckOf52()
