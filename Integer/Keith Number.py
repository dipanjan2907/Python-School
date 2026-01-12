n=int(input("Enter number: "))
n1=n
l1=[]
while(n>0):
    l1.append(n%10)
    n//=10
l1.reverse()
s,p,f=0,0,0
while(s<=n1):
    s=0
    for i in l1:
        s=s+i
    if s==n1:
        f=1
        break
    l1.pop(p)
    l1.append(s)
if f==1:
    print(n1," is Keith Number.")
else:
    print(n1," is not a Keith Number.")