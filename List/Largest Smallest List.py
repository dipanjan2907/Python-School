l=[]
m=int(input("How many elements to enter?: "))
for i in range(0,m):
    n=int(input("Enter number: "))
    l.append(n)
l.sort()
print("Smallest: ",l[0],"\nLargest: ",l[len(l)-1])