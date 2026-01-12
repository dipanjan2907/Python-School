l1=[]
l=int(input("Enter limit(even): "))
if l%2==0 and l!=0:
    for i in range(0,l):
        n=int(input("Enter number: "))
        l1.append(n)
    for i in range(0,l,2):
        l1[i+1],l1[i]=l1[i],l1[i+1]
    print(l1)
else:
   print("Limit can't be zero or odd")