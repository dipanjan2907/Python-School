n=int(input("Enter number: "))
n2,flag=0,0
s=""
l1=[]
for i in range(1,4):
    s=s+str(n*i)
s1=int(s)
while(s1>0):
    r=s1%10
    l1.append(r)
    s1=s1//10
if 0 in l1:
     c=l1.count(0)
     while(c>0):
         l1.remove(0)
         c=l1.count(0)
l1.sort()
for i in l1:
 n2=(n2+i)*10
n2//=10
if(123456789==n2):
 print(n," is a FASCINATING number")
else:
 print(n," is NOT a FASCINATING number")
import COPYRIGHT
COPYRIGHT.copyright()
