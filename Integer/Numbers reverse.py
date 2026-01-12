l=int(input("Enter limit: "))
l1=[]
for i in range(0,l):
    n=int(input("Enter number: "))
    l1.append(n)
for i in range(0,l):
    n=l1[i]
    r=0
    while(n>0):
        n1=n%10
        n//=10
        r=n1+r*10
    l1[i]=r
print(l1)
