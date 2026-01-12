s=input("Enter String: ")
s=s+" "
s1=""
for i in range(0,len(s)):
    if s[i].isalpha():
        s1+=s[i]
    elif s[i]==" ":
        if s1[0] in ['A','a','E','e','I','i','O','o','U','u']:
            print(s1)
        s1=""