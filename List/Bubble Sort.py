l=int(input("Enter limit: "))
l1=[];
for i in range(1,l+1):
    print("Enter number ",i,end="")
    n=int(input(": "))
    l1.append(n);
for i in range(0,len(l1)-1):
 for j in range(0,len(l1)-i-1):
     if l1[j]<l1[j+1]:
       l1[j+1],l1[j]=l1[j],l1[j+1]
print("Sorted in Descending:")
for i in range(len(l1)):
 print(l1[i]," ",end="")
