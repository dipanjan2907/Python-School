f=open('Word.txt','r')
d=f.read()
w=d.split()
for i in w:
    if len(i)>5:
        print(i,end=", ")