n=int(input("Enter no.: "))
s=0
p=1
n2=n
while(n>0):
    r=n%10
    n=n//10
    s+=r
    p*=r
if s==p:
    print(n2," is a SPY no.")
else:
    print(n2," is a not SPY no.")
