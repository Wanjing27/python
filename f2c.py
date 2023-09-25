#Step 1: input (prompt and read --- two actions from one input() function!)
f = float(input("Type in the degrees F: "))

#Step 2: do something: the f2c calculation you just tested! 
c =  (f-32) * 5/9

#Step 3: report to your client using print – probably use complete sentences  
print(str(f) + " degrees F = " + str(c) + " degrees C ")

#Step 3-cooler: report to your client using print – probably use complete sentences  
degree_sym =  "\u00b0"
print(str(f) + degree_sym +"F = " + str(c) + degree_sym +"C")
