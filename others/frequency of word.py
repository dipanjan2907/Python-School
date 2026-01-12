s=input("Enter string: ")
s=s.upper()+" "
w1=""
l1=[]
for i in range(0,len(s)):
   if(s[i]!=" "):
      w1+=s[i]
   else:
      l1.append(w1)
      w1=""
print(l1)
for i in l1:
   c=0
   for j in l1:
      if(i==j):
         c+=1
   print(i," is present ",c," time(s).")
   while(c>0):
    l1.remove(i)
    c-=1