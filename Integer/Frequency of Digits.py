n=int(input("Enter number: "))
l1=[]
while n>0:
    l1.append(n%10)
    n//=10
for i in range(0,10):
    c=0
    for j in l1:
        if i==j:
            c+=1
    print(i," is present ",c," times.")
    