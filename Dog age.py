def age(age):
    if age==1:
        print("your dog is 15 years old in dog years.")
    elif age==2:
        print ("your dog is 21 years old in dog years. ")
    else:
        weight(age)
        
def main():
    calage=float(input("How is your dog old?"))
    age(calage)

        
def weight(age):
    rate=(age-2)
    lbs=float(input("what is your dog's weight in lbs?"))
    if lbs<=20:
        dogage=(rate*4)+21
        print ("your dog is"+str(dogage)+" years old in dog years.")
    elif lbs<=50:
        dogage=(rate*5)+21
        print ("your dog is"+str(dogage)+" years old in dog years.")
    elif lbs<=90:
        dogage=(rate*6)+21
        print ("your dog is"+str(dogage)+" years old in dog years.")
    elif lbs>=90:
        dogage=(rate*7)+21
        print ("your dog is"+str(dogage)+" years old in dog years.")
    else:
        print("error")
        
main()
