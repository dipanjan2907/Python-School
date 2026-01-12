n=int(input("Enter number: "))
l=[]
n1=n
while(n1!=0):
    l.append(n1%10)
    n1=n1//10
if(len(l)%2==0 and l==l[::-1]):
    print(n," is even pal number.")
else:
    print(n," is not even pal number.")