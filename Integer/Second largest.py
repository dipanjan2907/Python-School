n=int(input("Enter number: "))
n1=n
l1=[]
while(n1>0):
    l1.append(n1%10)
    n1//=10
l1.sort()
print(l1[len(l1)-2])