l=int(input("Enter limit: "))
l1=[]
for i in range(0,l):
    n=int(input("Enter number: "))
    l1.append(n)
for i in range(0,l):
    for j in range(0,l-i-1):
        if l1[j]<l1[j+1]:
            l1[j],l1[j+1]=l1[j+1],l1[j]
print("DESCENDING SORT: ",l1)
