s=input("Enter string: ")
s=s.lower()
s1=""
for i in range(0,len(s)):
    if i%2==0:
        s1+=s[i].upper()
    elif i%2!=0:
        s1+=s[i].lower()
    else:
        s1+=s[i]
print(s1)