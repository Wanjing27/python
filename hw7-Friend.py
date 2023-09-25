class Friend:
    
    def __init__(self, n, a, p):
        self.name = n
        self.age = a
        self.phoneNum = p

    def __str__(self):
        return(self.name + ", age: " + str(self.age) + ", phone number: " + self.phoneNum)


def main():
    print("Demos instantiation of 2 Friend objects from the same Friend class")
    print("Includes a __str__ method to print out information") 
    #1. make a friend
    #1. get all the info you need to make the friend
    name = input("what's your friends' name? ")
    age = int(input("age? "))
    phone = input("what is their phone number ? " )

    #2. use the constructor (__init__() ) to make the friend
    #   aka instantiate a Friend object using the Friend class
    friend1 = Friend(name,age,phone)

    #prettier print bc of __str__
    print(friend1)


main()    
