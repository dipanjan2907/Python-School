l=int(input("Enter limit: "))
l1=[]
for i in range(0,l):
    s=input("Enter string: ")
    l1.append(s)
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
for i in l2:
    c=0
    for j in l1:
        if(i==j):
            c+=1
    print(i," is present ",c," times.")

