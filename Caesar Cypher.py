def getAlphabet():
    alphabet=[]
    for i in range (65,91):
        letter=chr(i)
        alphabet.append(letter)
    return(alphabet)


offset=5
def createCode(alpha,offset):
    offset_list=[]
    for item in alpha:
        if (ord(item)//86)==0:
            letter=chr(offset+ord(item))
            offset_list.append(letter)
        else:
            loop= ord(item)%86
            letter=chr(offset+60+loop)
            offset_list.append(letter)
    return(offset_list)

def enCode(alpha,codeAlpha,letter):
    for item in letter:
        index=alpha.index(item)
        code=codeAlpha[index]
        print(code,end="")
        
def main():
    offest=input("how many letter backwards for your code?endter a number: ")
    letter=input(" what is your message ?: ").upper()
    alpha=getAlphabet()
    codeAlpha=createCode(alpha,offset)
    enCode(alpha,codeAlpha,letter)

def creat_dic(alpha,codeAlpha):
    code_list={}
    for i in range(0,26):
        code_list[alpha[i]]=codeAlpha[i]
    return (code_list)

def encode2(letter, code):
    for item in letter:
        print(code[item])

def main2():
    offest=input("how many letter backwards for your code?endter a number: ")
    alpha=getAlphabet()
    codeAlpha=createCode(alpha,offset)
    code=creat_dic(alpha,codeAlpha)
    letter=input(" what is your message ?: ").upper()
    encode2(letter,code)

main2()
