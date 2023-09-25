loot = 100
import time

def riddlecave(loot):

    print("You have come across...")
    time.sleep(3)
    print("... a dangerous dragon!")
    print("You must answer her riddle if you wish to keep your loot!")
    print("Her question is... Never resting, never still. Moving silently from hill to hill. It does not walk, run or trot, All is cool where it is not. What is it?")
    answer = input("What is your answer?   ").lower()

    if answer == "sunshine":
        print("You solved it, she sees your wit and rewards you with 80 loot!")
        loot = loot + 80

    else:
        print("You have failed and it will cost you....")
        time.sleep(4)
        print("99 loot!")
        loot =loot - 99


    return(loot)  
