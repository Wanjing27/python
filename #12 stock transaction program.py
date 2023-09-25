shares = int(input("what is the number of shares Joe purchased?"))
stock = int(input("what is the price paid per share?"))
stock_price = shares*stock
stockbroker = float(input("what is the percentage as a decimal of the amount Joe paid his stockbroker for commission"))
stockbroker_commission = (stock_price*stockbroker)
shares_sold = int(input("what is the number of shares Joe sold?"))
stock_sold = float(input("what is the price he sold per share?"))
stock_sold_price = shares_sold*stock_sold
stockbroker_sold = float(input("what is the percentage as a decinmal of the amount Joe paid his stockbroker from commission"))
stockbroker_sold_commission = (stock_sold_price*stockbroker_sold)
print("the amount Joe paid for the stock is $" +str(stock_price))
print("the amount of commission Joe paid his broker when he bought the stock is $" +str(stockbroker_commission))
print("the amount Joe sold the stock for is $" +str(stock_sold_price))
print("the amount of commission Joe paid his broker when he sold the stock is $" +str(stockbroker_sold_commission))
first_total = stock_price-stockbroker_commission
print("the amount of money Joe had left when he bought the stock and paid his stockbroker is $" +str(first_total))
second_total = stock_sold_price-stockbroker_sold_commission
print("the amount of money Joe had left when he sold the sock and paid his stockbroker is $" +str(second_total))

