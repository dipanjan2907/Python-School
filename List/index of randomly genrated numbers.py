l1=[]
f=0
import random
l=int(input("Enter max limit for number generation: "))
for i in range(0,20):
    l1.append(random.randint(0,l))
print(l1)
s=int(input("Enter number to be searched: "))
for i in range(0,20):
    if(s==l1[i]):
        print(l1.index(s))
        f=1
if (f==0):
    print("number not present.")