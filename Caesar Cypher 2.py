joke="Knock , Knock . Who's there ? Banana . Banana , who ? Banana , Knock Knock . Who's there ? Banana . Banana , who ? Banana , Knock Knock . Who's there ? Banana . Banana , who ? Banana , Knock Knock . Who's there ? Orange . Orange who ? Orange you glad I didn't say Banana again ?  "
joke_list=joke.split()
dic={"Knock":"hi",",":"!","Who's":"what's","there":"that","?":"*","Banana":"me",".":"?","who":"what","?":".","Orange":"you","you":"should","glad":"be","I":"happy","didn't":"about","say":"to see", "again":"again"}
for item in joke_list:
    print(dic[item],end=' ')
