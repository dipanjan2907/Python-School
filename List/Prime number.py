l=int(input("How many numbers do you want to enter? :"))
l1=[]
for i in range(0,l):
    n=int(input("Enter number: "))
    l1.append(n)
flag=0
c=0
for i in l1:
    for j in range(1,i+1):
        if(i%j==0):
            c=c+1
    if (c==2):
        print(i," is prime number")
        flag=1
    c=0
if flag==0:
    print("No prime numbers")
