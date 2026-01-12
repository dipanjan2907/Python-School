s=input("Enter sentence: ")
s=s.upper()+" "
c=0
s1=""
l1=[]
for i in range(0,len(s)):
    if(s[i]==" "):
        if(s1==s1[::-1]):
            c+=1
        s1=""
    else:
        s1+=s[i]
print(c," palindrome words")