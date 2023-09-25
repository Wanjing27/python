def main():
    wordCount = dict()   #make an empty dictionary
    f = open("bestOfTimes.txt","r") #open up a file

    for line in f:                 #pull each line from the file
        words = line.split(' ')    #split the line based on spaces and put the words in a lists
        for word in words:         # take each word from the list of words
            word=word.lower()      # make it all lower case (to compare to others)
            print ("word: " + word)
            if word in wordCount:
                wordCount[word]+=1
            else:
                wordCount[word]=1
    report(wordCount)

def report(wordCount):
    for k in wordCount:
        print(k + ": " + str(wordCount[k]))
     
main()
