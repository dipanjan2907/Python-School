s=input("Enter word: ")
s=s.upper()
s1=""
for i in range(0,len(s)):
    if(s[i]=='A' or s[i]=='O' or s[i]=='E' or s[i]=='I' or s[i]=='U'):
        s1+=s[i]
l1=list(s1)
for j in range(1,len(l1)):
    for i in range(1,len(l1)):
            if(ord(l1[i-1])>ord(l1[i])):
                t=l1[i]
                l1[i]=l1[i-1]
                l1[i-1]=t
for i in l1:
    print(i,end=" ")
