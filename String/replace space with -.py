s=input("Enter String: ")
s1=""
for i in range(0,len(s)):
    if s[i].isalpha():
        s1+=s[i]
    elif s[i]==" ":
        s1+="-"
print(s1)