n=int(input("Enter number: "))
n1=n
sq=n*n
c=0
while n1>0:
    n1=n1//10
    c+=1
if sq%(10**c)==n:
 print(n," is an AUTOMORPHIC NUMBER")
else:
    print(n," is NOT an AUTOMORPHIC NUMBER")
 
