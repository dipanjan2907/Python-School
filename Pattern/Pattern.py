l1=['A','B','C','D','E']
s=4
l=0
for i in range(1,6):
   for j in range(1,s+1):
       print(" ",end=" ")
   for k in range(l,-1,-1):
       print(l1[k],end=" ")
   print(" ")
   s-=1
   l+=1
