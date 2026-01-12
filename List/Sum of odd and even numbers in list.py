l1=[]
l=int(input("How many elements do you want?: "))
for i in range(0,l):
    n=int(input("Enter number: "))
    l1.append(n)
se=0
so=0
for i in l1:
    if (i%2==0):
        se+=i
    else:
        so+=i
print("Sum of even numbers: ",se)
print("Sum of odd numbers: ",so)
