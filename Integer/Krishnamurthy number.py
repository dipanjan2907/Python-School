n=int(input("Enter no."))
t=n
sum=0
while t>0:
 r=t%10
 t=t//10
 f=1
 while r>0:
     f=f*r
     r-=1
 sum+=f
if sum==n:
 print(n," is a Krishnamurthy number")
else:
 print(n," is not a Krishnamurthy number")
