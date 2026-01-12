n=int(input("Enter number: "))
n1=n
n2=n
c=0
s=0
while n>0:
    n//=10
    c+=1
while n1>0:
    r=(n1%10)**c  #** denotes power
    n1//=10
    s+=r
if s==n2:
    print(n2," is an ARMSTRONG number.")
else:
    print(n2," is not an ARMSTRONG number.")
