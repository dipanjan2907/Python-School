s=input("Enter string: ")
v,c,l,u=0,0,0,0
l1=['A','E','I','O','U','a','e','i','o','u']
for i in range(0,len(s)):
    for j in range(0,len(l1)):
        if(s[i]==l1[j]):
            v+=1
            break
    if(s[i].isupper()):
        u+=1
    elif(s[i].islower()):
        l+=1
    else:
        c+=1
print("Vowels= ",v)
print("Consonants= ",c)
print("Upper Case= ",u)
print("Lower Case= ",l)