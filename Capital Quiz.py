import random
statesCap={"Alabama":"Montgomery", "Alaska":"Juneau", "Arizona":"Phoenix", "Arkansas": "Little Rock", "California": "Sacramento", "Colorado":"Denver", "Connecticut":"Hartford", "Delaware": "Dover", "Florida": "Tallahassee", "Georgia": "Atlanta","Hawaii":"Honolulu" ,"Idaho": "Boise","Illinois": "Springfield", "Indiana": "Indianapolis", "Iowa":"Des Moines", "Kansas":"Topeka", "Kentucky": "Frankfort", "Louisiana": "Baton Rouge", "Maine": "Augusta", "Maryland": "Annapolis", "Massachusetts": "Boston", "Michigan": "Lansing", "Minnesota":"St. Paul", "Mississippi": "Jackson", "Missouri": "Jefferson City", "Montana": "Helena", "Nebraska": "Lincoln", "Nevada": "Carson City", "New Hampshire": "Concord", "New Jersey": "Trenton", "New Mexico": "Santa Fe", "New York": "Albany", "North Carolina": "Raleigh", "North Dakota" :"Bismarck", "Ohio": "Columbus", "Oklahoma": "Oklahoma City", "Oregon": "Salem", "Pennsylvania": "Harrisburg", "Rhode Island": "Providence", "South Carolina": "Columbia", "South Dakota": "Pierre", "Tennessee": "Nashville", "Texas": "Austin", "Utah" : "Salt Lake City", "Vermont":"Montpelier", "Virginia": "Richmond", "Washington": "Olympia", "West Virginia": "Charleston", "Wisconsin": "Madison", "Wyoming":"Cheyenne"}
state=[]
for key in statesCap:
    state.append(key)
    
i=0
socre=0
while i<2:
    gstate=state[random.randint(1,10)]
    print(statesCap[gstate])
    answer=input("What is the capital of "+state[random.randint(1,10)]+":")

    if answer==statesCap[gstate]:
        print("correct")
        i=+1
        score=+1
    else:
        print('wrong')
        i=+1

print("score: "+score)
