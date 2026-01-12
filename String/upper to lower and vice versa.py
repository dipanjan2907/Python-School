s=input("Enter a sentence: ")
ns=""
for i in range(0,len(s)):
    if ord(s[i])>=65 and ord(s[i])<=90:
        ns=ns+s[i].lower()
    elif ord(s[i])>=97 and ord(s[i])<=122:
        ns=ns+s[i].upper()
    else:
        ns=ns+s[i]
print("Modified String: ",ns)
