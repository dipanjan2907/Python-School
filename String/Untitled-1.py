s=input("Enter String: ")
c=0
for i in range(0,len(s)):
    if s[i] not in 'AEIOUaeiou':
        c+=1
print(f"Total {c} characters")

#8- Check if length of both strings EQUAL