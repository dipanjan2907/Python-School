l=int(input("Enter limit [even]: "))
l1=[]
l2=[]
l3=[]
l4=[]
for i in range(0,l):
    n=int(input("Enter number: "))
    l1.append(n)
for i in range(0,l//2):
    l2.append(l1[i])
l2.sort()
for i in range(l//2,l):
    l3.append(l1[i])
l3.sort()
for i in range(-1,-1*(l//2+1),-1):
    l4.append(l3[i])
print(l2+l4)
