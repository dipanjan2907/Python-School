f=open("Word.txt","r")
c=False
for l in f:
    for i in l.split():
        if i.startswith("p") or i.startswith("P"):
            c=True
            print(i)      
if c==False:
    print("No such words")
f.close()
        