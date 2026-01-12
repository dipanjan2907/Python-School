n=int(input("Enter a no.: "))
s=0
for i in range (1,n):
 if n%i==0:
  s+=i
if s==n:
    print(n," is a perfect no.")
elif s>n:
    print(n," is an abundant no.")
else:
    print(n," is a deficient no.")
