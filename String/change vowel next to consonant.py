s=input("Enter word: ")
s=s.upper()
s1=""
for i in range(0,len(s)):
    if(s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U'):
        l=ord(s[i])
        s1+=chr(l+1)
    else:
        s1+=s[i]
print(s1)