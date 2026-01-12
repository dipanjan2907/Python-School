l=int(input("Enter limit [even]: "))
l1,l2=[],[]
for i in range(0,l):
    n=int(input("Enter number: "))
    l1.append(n)
for i in range(1,l,2):
    l3=[int(z) for z in str(l1[i])]
    z=len(l3)
    l2.append((l1[i-1]*(10**z))+l1[i])
print(l2)