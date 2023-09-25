class Player:
    
    def __init__(self, n , g=0):
        self.name = n
        self.gamesWon = 0  # note: when you create this Player, they haven't won any games yet

    def __str__(self):
        return(self.name + ", games won: " + str(self.gamesWon) )


def main():
    print("Demos instantiation of a Player object from the same Player class")
    print("Includes a __str__ method to print out information") 
    #1. make two players
    #1. get all the info you need to make the friend
    name1 = input("what's the players' name? ")
    name2 = input("What's teh second player's name? ")
 
    #2. use the constructor (__init__() ) to make the player
    #   aka instantiate two Player objects using the Player class
    player1 = Player(name1)
    player2 = Player(name2)
    #prettier print bc of __str__
    print(player1, end = "  ")
    print(player2)

    #give player 1 a point
    player1.gamesWon +=1

    print(player1, end = "  ")
    print(player2)


main()    
