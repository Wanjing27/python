# program to tell your client how much of each ingredient to ues to make N cookies

#INPUT -- number of cookies wanted. Need to convert the keyboard string to a number 
cookies = int(input("how many cookies would you like to make?"))

#calcuations
#get the amounts for just one cookie from the documented amounts for 48 cookies
sugarForOne = (1.5/48)
butterForOne = (1/48)
flourForOne = (2.75/48)

#figure out the amounts for desired number of cookies
sugarTotal = sugarForOne * cookies
butterTotal = butterForOne * cookies
flourTotal = flourForOne * cookies

#REPORT / print need to convert numbers to printable strings
print("the amount of cups of sugar: " +str(sugarTotal) + " cups")
print("the amount of cups of butter: " +str(butterTotal) + " cups")
print("the amount of cups of flour: " +str(flourTotal) + " cups")
