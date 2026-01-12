n=int(input("enter no.: "))
for a in range(2,n+1):
     if n%a==0:
      break
if a==n:
    print ("prime")
else:
    print("not prime")
