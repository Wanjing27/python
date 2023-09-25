class Friend:
    def __init__(self,n,a,p):
        self.name=n
        self.age=a
        self.number=p
    def __str__(self):
        return(self.name+ " age: "+str(self.age)+" number: "+str(self.number))
    def __repr__(self):
        return str(self)

def main():
    friends=int(input("how many friends do you have ? "))
    friend_list=[]
    for i in range (friends):
        name=input("what's your friends' name? ")
        age=int(input("age? "))
        number=int(input("phone number ? "))
        friend=Friend(name,age,number)
        friend_list.append(friend)
    print(friend_list)
main()
