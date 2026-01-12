n=int(input("Enter no.:"))
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print(n," is a prime no.")
else:
    print(n," is not prime no.")
