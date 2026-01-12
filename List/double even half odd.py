def  AdjustValues(l1):
    for i in range(len(l1)):
        if l1[i]%2==0:
            l1[i]*=2
        else:
            l1[i]/=2   
    print(l1)
l=int(input("Enter the length of the list: "))
l1=[]
for i in range(l):
    l1.append(int(input("Enter number: ")))
AdjustValues(l1)