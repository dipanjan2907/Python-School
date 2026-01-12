s1=input("Enter string: ")
s2=""
for i in range(0,len(s1)):
    if(s1[i]==" "):
        s2+="@"
    else:
        s2+=s1[i]
print(s2)