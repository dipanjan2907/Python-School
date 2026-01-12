s=input("Enter string:")
s=" "+s
c=0
for i in range(0,len(s)):
    if s[i]==" ":
        c+=1
    k=i
    if  s[i]==" " and c%2!=0:
        k-=1
        while s[k]!=" " and k>0:
            print(s[k],end="")
            k-=1
        print("",end=" ")