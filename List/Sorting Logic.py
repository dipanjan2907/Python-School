list1=[11,13,14,10,9,8,12]
n=len(list1)
for i in range(0,n-1):
 for j in range(i+1,n):
     if list1[i]>list1[j]:
      list1[i],list1[j]=list1[j],list1[i]
for i in range(n):
 print(list1[i]," ",end="")
