n1=int(input("Enter number: "))
n2=0
tn1=n1
while(tn1>0):
    n2=n2*10
    n2+=(tn1%10)
    tn1//=10
c1,c2=0,0
for i in range(1,n1+1):
    if(n1%i==0):
        c1+=1
for i in range(1,n2+1):
    if(n2%i==0):
        c2+=1
if(c1==2 and c2==2):
    n1sq=n1*n1
    n2sq=0
    tn1sq=n1sq
    while(tn1sq>0):
        n2sq*=10
        n2sq+=(tn1sq%10)
        tn1sq//=10
    if(n2sq==n2*n2):
        print(n1,"is an PrimeAdam number.")
    else:
        print(n1,"is not an PrimeAdam number.")
else:
    print("Not a prime number.")
