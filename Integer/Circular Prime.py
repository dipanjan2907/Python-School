n=int(input("Enter number: "))
f,n3,n4=0,0,0
n1=n
n2=0
l1=[]
while n1>0:
    l1.append(n1%10)
    n1//=10
l1.sort()
for i in range(len(l1)-1,-1,-1):
    n2=(n2+l1[i])*10
n2//=10
for i in range(0,len(l1)):
    n3=(n3+l1[i])*10
n3//=10
for i in range(1,n2+1):
    c,n4=0,0
    k=i
    l2=[]
    while i>0:
        l2.append(i%10)
        i//=10
    l2.sort()
    for a in range(0,len(l2)):
        n4=(n4+l2[a])*10
    n4//=10
    if(n3==n4):
        for j in range(1,k+1):
            if(k%j==0):
                c+=1
        if(c==2):
            f=1
        else:
            f=0
if(f==1):
    print(n," is a cicular prime number.")
else:
    print(n," is not circular prime number.")