loot = 100
import time
def pickadoor(loot):
    print("You have encountered 3 doors, you must pick which one you wish to go into...")
    door=input("Which door will you enter, 1 2 or 3?  ")

    if door == '1':
        print("....")
        time.sleep(2)
        print("Good choice you found a chest, you have now just gained 30 more loot!")
        loot=loot + 30

    elif door == '2':
        print("....")
        time.sleep(2)
        print("Poor descion, the robbers behind the door saw your money, and robbed you! You just lost a fortune, 50 loot!!")
        loot =loot - 50

    elif door == '3':
        print("....")
        time.sleep(2)
        print("You found the exit, you leave unscathed but with no additional loot")
        

    else:
        print("That's not an option for a door you trickster!")
        print("The cave collapses on you and you have to dig your way out.")
        print("You drop a lot of loot on the way out and you come out broke and broken")
        loot = loot-500

    

    return(loot)


