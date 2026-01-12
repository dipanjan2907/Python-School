n=int(input("Enter number: "))
nc=n
n1=0
while nc>0:
 n2=nc%10
 nc=nc//10
 if n1<n2:
  n1=n2
print("Largest=",n1)
n1=9
while n>0:
 n2=n%10
 n=n//10
 if n1>n2:
  n1=n2
print("Smallest=",n1)
            
