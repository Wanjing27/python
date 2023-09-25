def for_in():
    list1=[]
    for i in range(0,101,2):
        list1.append(i)
    print (list1)   


def w():
    i=-1
    list2=[]
    while i<=100:
        i+=1
        if i%2==0:
            list2.append(i)
    print(list2)



def for_item():
    numbers=list(range(0,101))
    even=[]
    for item in numbers:
        if item%2==0:
            even.append(item)
    print(even)
