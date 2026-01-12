l1=[]
for i in  range(0,5):
    n=int(input("Enter number: "))
    l1.append(n)
l2=[]
for i in range(0,5):
    n1=l1[i]
    n2=0
    while(n1>0):
        n2*=10
        n2=n2+(n1%10)
        n1//=10
    l2.append(n2)
print(l2)