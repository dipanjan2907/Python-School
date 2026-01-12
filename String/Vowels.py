s=input("Enter word/sentence: ")
s=s.upper()
c=0
for i in s:
    if(i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        c+=1
print("There are ",c," vowels")
