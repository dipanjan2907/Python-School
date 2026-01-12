n=int(input("Enter digit count: "))
for i in range(10**(n-1),10**n):
 fc=0
 pc=0
 for j in range(1,i+1):
  if i%j==0:
   fc+=1
 if fc==2:
  pc+=1
  print(i)
print("There are ",pc," ",n,"-digit prime number(s)")
