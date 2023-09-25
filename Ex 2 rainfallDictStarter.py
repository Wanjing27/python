def main():
    #rainfall for the months of a year
    #New Way: do what you did in two lists in one dictionary

    ################Build the dictionary: code months directly as keys ###############
    #Start with one with 0 values. These will be replaced with rainfall amounts
    rfDict = {"Jan":0, "Feb":0, "Mar":0}
 
    keys = rfDict.keys()   		# extracts all the keys
    for key in keys:
        rf = float(input("What was the rainfall in " + key + "?  "))
        # (1) put the new value in the right place in the dictionary
        rfDict[key]=rf
    print (rfDict)

    ################ Use the dictionary  ########################
    #find the total rainfall for all months
    values = rfDict.values()# extracts all the values
    total=0
    for values in values:
        total=total+values
   
    #(2) loop code to total all values goes here
        
    print(str(total))
main()
