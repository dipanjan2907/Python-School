l1=[]
for i in range(0,5):
    n=int(input("Enter odd number: "))
    if(n%2!=0):
        l1.append(n)
    else:
        print("Odd numbers only")
        i-=1
print("")
l2=[]
for i in range(0,4):
    n=int(input("Enter even number: "))
    if(n%2==0):
        l2.append(n)
    else:
        print("Even numbers only")
        i-=1
l1.insert(2,l2)
print(l1)