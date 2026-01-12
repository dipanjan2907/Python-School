import COPYRIGHT
l=int(input("How many names to enter?: "))
l1=[]
d1=dict()
r=0
for i in range(0,l):
    n=input("Enter name: ")
    n.upper()
    l1.append(n)
l2=sorted(l1)
for i in range(0,l):
    print("Roll number ",i+1,". ",l2[i])
COPYRIGHT.copyright()
