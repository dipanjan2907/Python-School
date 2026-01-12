l=int(input("Enter limit: "))
l1=[];
for i in range(1,l+1):
    print("Enter number ",i,end="")
    n=int(input(": "))
    l1.append(n);
for i in range(0,len(l1)-1):
 for j in range(i+1,len(l1)):
     if l1[i]>l1[j]:
        l1[i],l1[j]=l1[j],l1[i]
print("Sorted in Ascending:")
for i in range(len(l1)):
 print(l1[i]," ",end="")
