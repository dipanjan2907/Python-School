import random
l=int(input("Enter limit: "))
l1=[]
for i in range(0,l):
    l1.append(random.randint(10,999))
print("\nOriginal List: ",l1)
for i in range(0,l):
    s=0
    n2=0
    if(l1[i]%2!=0):
        while(l1[i]>0):
            r=l1[i]%10
            l1[i]=l1[i]//10
            n2=n2*10+r
        l1[i]=n2
    else:
        while(l1[i]>0):
            r=l1[i]%10
            l1[i]=l1[i]//10
            s+=(r*r)
        l1[i]=s
print("\nModified List: ",l1)
