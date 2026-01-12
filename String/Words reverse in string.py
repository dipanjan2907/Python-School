s=input("Enter string: ")
s+=" "
w1,w2="",""
for i in range(0,len(s)):
    if(s[i]!=" "):
        w1+=s[i]
    else:
        w2=w2+w1[::-1]+" "
        w1=""
print(w2)
