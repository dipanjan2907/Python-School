l=int(input("How many numbers to enter?: "))
l1=[]
for i in range(0,l):
    n=int(input("Enter number: "))
    l1.append(n)
for i in range(1,l):
    if(l1[i-1]>l1[i]):
        g=l1[i-1]
    else:
        g=l1[i ]
for i in range(1,l):
    if(l1[i-1]<l1[i]):
        l=l1[i-1]
    else:
        l=l1[i]
print("Greatest= ",g)
print("Smallest= ",l)
