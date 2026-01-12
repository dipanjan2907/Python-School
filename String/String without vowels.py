s=input("Enter word/sentence: ")
s=s.upper()
for i in s:
    if(i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        s=s.replace(i,"")
print("Without Vowels: ",s)
