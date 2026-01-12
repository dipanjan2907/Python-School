l=int(input("Enter limit: "))
l1=[]
for i in range(0,l):
    n=int(input("ENTER NUMBER: "))
    l1.append(n)
for i in range(0,l):
    for j in range(1,l):
        if(l1[j-1]>l1[j]):
            l1[j-1],l1[j]=l1[j],l1[j-1]
print("Max: ",l1[l-1])
print("Min: ",l1[0])