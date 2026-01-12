s=input("Enter String: ")
c=input("Enter character to delete: ")
s1=""
for i in range(0,len(s)):
    if s[i]!=c:
        s1+=s[i]
print(s1)