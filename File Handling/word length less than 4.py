def displaywords():
    l1=[]
    f=open("Story.txt","r")
    for l in f:
        l1.extend(l.replace("\n"," ").split(" "))
    for i in l1:
        i=i.strip()
        if(len(i)<4 and i!=""):
            print(i,end=", ")
    f.close()
displaywords()

#In, a, we, The, us, on, are, day, new, in, the, of, the, the, at, our, to, its,