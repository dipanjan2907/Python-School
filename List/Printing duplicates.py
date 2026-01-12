l1=[]
l=int(input("Enter limit: "))
for i in range(0,l):
    print(i+1,end="")
    l1.append(int(input(".")))
for i in l1:
    c=0
    for j in l1:
        if(i==j):
            c+=1
    if(c>1):
        print(i," is a duplicate")
    while(c>0):
        l1.remove(i)
        c-=1