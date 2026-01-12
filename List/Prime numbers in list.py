n=int(input("Enter number: "))
n1=n
l1=[]
while(n1!=0):
    r=n1%10
    l1.append(r)
    n1//=10
p=0
for i in l1:
   c=0
   for j in range(1,i+1):
       if(i%j==0):
           c+=1
   if (c==2):
       p+=1
print("\n",p," prime numbers in number ",n)
