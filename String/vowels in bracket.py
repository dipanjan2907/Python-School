s=input("Enter string: ")
s1=""
for i in range(0,len(s)):
    if(s[i] not in "AaEeIiOoUu"):
        s1+=s[i]
    else:
        s1+="("+s[i]+")"
print("VOWELS IN BRACKET: ",s1)