# cave 1
loot=50
import time
#input;loot
def chest_cave1(loot):
    print ("you have encounter...")
    time.sleep(3)
    print ("a friendly dragon.")
    print("He offer you a key, and three treasure chests. "
          "There is a gold treasure chest, a silver treasure chest, a wooden treasure chest.")
    #process; make options; gain or lost loots
    chest=input(" Which chest do you choose to open? Gold? Silver? or wooden?").lower()
    if chest=="gold":
        print("there's noting in the chest, the dragon said he spent all the loot to make that chest.")
    elif chest=="silver":
        print("you gain 20 loots")
        loot=loot+20
    elif chest=="wooden":
        print("You found a massive hole in the chest with some weird smelly creature in it. The dragon felt terrible and give you 40 loots.")
        loot=loot+30
    else:
        print("You throw away the key, and the dragon got mad as an act of revenge he threw you in the river. You lost 60 loots.")
        loot=loot-60
    #output loots
    return (loot)



            
