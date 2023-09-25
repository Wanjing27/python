# program to determine how far a car has traveled in a specific time given its speed

#INPUT: speed and time traveled 
# get the speed from the client (convert keyboard string to integer)
speed = int(input("how fast is your car traveling?"))
# get the time traveled from the client
time = int(input("how long will you be travleing?"))

# calculation: rate x time is distance
distance = speed*time

# REPORT/ print (convert distance to a string to print to screen) 
print("the distance you will travel is " +str(distance))
