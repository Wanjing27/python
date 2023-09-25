import random
import time

def main():
    introduction()
    # give the player some starting loot
    loot = 50
    turns = 0  # you will probably change this so that the player can stop early
                #or the game can stop them if they have negative loot
    while turns < 3:
        turns = turns + 1 
        cavenumber = choosecave()
        print(cavenumber) # good for debugging. Perhaps improve or remove later
        
        if(cavenumber == 1):
            loot = friendly(loot)
        elif (cavenumber > 1):  # Persons 3-6 will write additional elif caves
            print("These caves haven't been dug yet")
        else:
            print("you're dead!")

    if(loot<=0):
        print("sorry that you died in the game!")
    else:
        print("What! Quiting? No guts! No glory!")
    


def friendly(loot):
    #cave number 1: friendly
    #customize before turning in
    print ("You have encountered...")
    time.sleep(3)
    print("...the friendly dragon!")
    print("She has given you treasure!")
    loot= loot + random.randint(1,11)
    #customize before turning in 
    print ("and you now have " + str(loot)+ " gold coins!")
    return(loot)



def introduction():
    print("Tell the player how to play! ")

def choosecave():
        print("Here's where you will set up a random number generator to pick a cave number")
        cave = 1  # right now the cave is always cave number 1
        return cave

def report(lootLeft):
    print("based on the lootLeft, tell the player whether they leave the game broke or rich!")
    

main()




