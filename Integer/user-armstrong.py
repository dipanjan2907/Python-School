n=int(input("Enter digit count: "))
c=0
for i in range(10**(n-1),10**n):
 i1=i
 s=0
 while i1>0:
  r=(i1%10)**n
  s+=r
  i1=i1//10
 if s==i:
  print(i)
  c+=1
if c>0:
 print("There are ",c," ARMSTRONG NUMBERS")
else:
 print("There are NO ARMSTRONG NUMBERS")
