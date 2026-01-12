l=int(input("Enter limit: "))
l1=[]
for i in range(0,l):
    s=input("Enter word: ")
    s=" "+s
    l1.append(s)
l2=[]
for i in range(0,l):
    t=l1[i]
    for j in range(1,len(t)):
        if(t[j-1]==" " and t[j]!=" "):
            l2.append(t[j])
print(l2)