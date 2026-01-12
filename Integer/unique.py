n=int(input("Enter number: "))
ns=str(n)
f=0
for i in ns:
    c=0
    for j in ns:
        if i==j:
            c+=1
    if c>1:
        f=1
        break
if f==1:
    print("Not Unique")
else:
    print("Unique")