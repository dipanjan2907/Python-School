l=int(input("How many numbers to enter?: "))
l1=[]
for i in range(0,l):
    n=int(input("Enter number: "))
    l1.append(n)
l1.sort()
for i in range(l-1,-1,-1):
    print(l1[i])
