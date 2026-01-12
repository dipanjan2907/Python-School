l1=[0,1]
a,b=0,1
l=int(input("Enter nth number: "))
while(len(l1)<=l):
    l1.append(l1[a]+l1[b])
    a=b
    b=b+1
print("Term ",l," of Fibonacci series: ",l1[l-1])