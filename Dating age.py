#calculate range
def age_range(age):
   youngest=(age/2+7)
   oldest=((age-7)*2)
   print(" your range of dating is from "+str(youngest)+" to "+str(oldest))
   return youngest, oldest

#main function
def creepy_dating():
   name1=input("hi, what is your name?")
   age1=float(input("what is your age?"))
   if age1<=14:
      print("you are too young to date")
   else:
      age_range(age1)
      dating(age1)
   

# see of it a fit
def dating(age):
   youngest=(age/2+7)
   oldest=((age-7)*2)
   i=0
   while i<3:
      name2=input(" what s your crush's name ?")
      age=float(input("what is your crush's age ?"))
      if age<youngest:
         print(name2+" is too young for you")
      elif age>oldest:
         print(name2+" is too old for you")
      else:
         print ( "your guys are meant to be" )
      if i!=3:
         again=input("do you have any other crush? y/n ").lower()
         while again!="n" and again!="y":
            print("error, try again")
         if again=="y":
            print("okay")
            i=i+1
         else:
            print("cool")
            i=i+4

creepy_dating()
