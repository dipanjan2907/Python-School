n=int(input("Enter limit: "))
a=0
b=1
for i in range(1,n+1):
    print(a,end=" ")
    c=a
    a=b
    b=a+c 