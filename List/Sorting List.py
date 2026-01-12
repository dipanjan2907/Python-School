l=int(input("How many numbers do you want to enter?: "))
l1=[]
for i in range(0,l):
    n=int(input("Enter number: "))
    l1.append(n)
for i in range(0,l+1):
    for j in range(1, l-i):
        if (l1[j-1]>l1[j]):
            t=l1[j-1]
            l1[j-1]=l1[j]
            l1[j]=t
print("Sorted list")
for i in l1:
    print(i)
