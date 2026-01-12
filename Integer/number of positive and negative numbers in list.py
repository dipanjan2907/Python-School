l1=[]
l=int(input("How many elements do you want?: "))
for i in range(0,l):
    n=int(input("Enter number: "))
    l1.append(n)
p=0
n=0
for i in l1:
    if (i>0):
        p+=1
    elif(i<0):
        n+=1
print(p," positive number(s)")
print(n," negative number(s)")
