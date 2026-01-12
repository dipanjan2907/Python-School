l1=[]
l=int(input("How many elements do you want?: "))
for i in range(0,l):
    n=int(input("Enter number: "))
    l1.append(n)
p=1
for i in l1:
    p=p*i
print("Product of elements= ",p)
