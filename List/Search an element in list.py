l1=[]
l=int(input("How many elements do you want to enter?: "))
for i in range(0,l):
    n=int(input("Enter element: "))
    l1.append(n)
s=int(input("Enter element to be searched: "))
flag=0
for i in range(0,len(l1)):
    if (s==l1[i]):
        print(s," found at index ",i)
        flag=1
        break;
if(flag==0):
    print(s," not present!")
