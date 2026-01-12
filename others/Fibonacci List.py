l1=[0,1]
a=0
b=1
l=int(input("Enter limit: "))
for i in range(1,l-1):
    l1.append(l1[a]+l1[b])
    a=b
    b=b+1
print(l1)
