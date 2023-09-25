
#input;loot
#process: make a decision; takes loot or take away loot
# output; loot

loot=50
def bad_dragon1(loot):
    print ("you have encounter...")
    time.sleep(3)
    print (" a sleeping dragon. Right next to him there's 50 loots.")
    sleep=input(" want to wake up the dragon? y/n ").lower()
    while sleep!="n" and sleep!="y":
        print("error, try again")
        sleep=input(" want to wake up the dragon? y/n ").lower()
    if sleep=="y":
        print("You woke up the dragon from his nap, and he is angry...oh no... RUN!!!!")
        time.sleep(2)
        print("While you are running away from the dragon, you slipped and fell on your face...you lost 25 loots.")
        loot=loot-25
    elif sleep=="n":
        print(" What!!  Are you trying to sneak next to him and steal thoes loot... *whisper *no! You will wake him up!! I can't watch this...")
        chance=random.randint(1,2)
        time.sleep(3)
        if chance!=1:
            print("Dragon:ROOAAARR")
            print("You steped on the dragon's tail, he must be pissed .")
            print("The dragon made you pay 30 loots and throw you out of the cave.")
            loot=loot-30
        else:
            print("You successfully steal 45 loots from the dragon without waking up him up.")
            print("lucky you")
            loot=loot+45
    return( loot)
