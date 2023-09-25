# input
number=int(input("Enter an interger to find out all numbers that is evenly divisible: "))
for i in range(1,101):
    if i%number==0:
        print(str(i))
print( "that's all the available number from 1 to 100")
