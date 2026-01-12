n=int(input("Enter number: "))
f=0
print("PRIME NUMBERS IN RANGE OF ",n**2," and ",(n+1)**2)
for i in range(n**2,((n+1)**2)+1):
    c=0
    for j in range(2,i+1):
        if i%j==0:
            c+=1
    if c==2:
        print(i)
        f=1
if f==0:
    print("NONE")
