def main():
    f = open('girlBabyNamesShort2Test.txt','r')
    lines = f.readlines()
    f.close()

    print("there are " + str(len(lines)) +  " names in the list")
    print("and " + lines[0] + " is the first")
    
    for line in lines:
        print("####" +line+"####")
        #there's an invisible new line at the end of the line. Use strip to get rid of it
        line = line.strip()
        print("####" +line+"####")
        wait = input("hit any key to continue")

