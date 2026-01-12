l=int(input("Enter limit: "))
l1=[]
flag=0
for i in range(0,l):
    print("Enter number ",i+1,end="")
    n=int(input(": "))
    l1.append(n)
s=int(input("Enter number to be searched: "))
for i in range(0,l):
    if s==l1[i]:
        print(s," is present at index ",i)
        flag=1
        break
if flag==0:
    print(s," not found.")
