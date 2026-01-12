l=int(input("Enter limit: "))
n1=[];
for i in range(1,l+1):
    print("Enter number ",i,end="")
    n=int(input(": "))
    n1.append(n)
for i in range(0,len(n1)):
    for j in range(0,n1[i]+1):
        if(j*j==n1[i]):
            print(n1[i])
