l=int(input("Enter limit: "))
print("Automorphic numbers")
flag=0
for i in range(1,l+1):
 c=0
 i1=i
 while i1>0:
  i1=i1//10
  c+=1
 if i==(i*i)%(10**c):
  print(i)
  flag=1
if flag==0:
 print("ERROR!! There are no automorphic numbers between ",1," and ",l,"")

