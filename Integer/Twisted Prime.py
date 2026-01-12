n1=int(input("Enter number: "))
n=n1
n2=0
while(n1>0):
    r=n1%10
    n1=n1//10
    n2=n2*10+r
c1=0
f1=0
for i in range(1,n+1):
    if (n%i==0):
        c1+=1
if(c1==2):
    f1=1
c2=0
f2=0
for i in range(1,n2+1):
    if (n2%i==0):
        c2+=1
if(c2==2):
    f2=1
if(f1==1 and f2==1):
    print("TWISTED Prime")
else:
    print("Not Twisted Prime")
