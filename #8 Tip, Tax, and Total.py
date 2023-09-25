# Tip, Tax, and Total
price=float(input("type the total charge for the food: "))
tip=price*.18
tax= price*.07
total=price+tip+tax
print("subtotal: $"+str(price))
print("tips: $"+str(format(tip, '20.2f')))
print("tax: $"+ str(format(tax,'.2f')))
print("total price: $" +str(total))
