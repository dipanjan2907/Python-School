s=input("Enter word/sentence: ")
s1=" "
for i in s:
    if(i.isupper()):
        i=i.lower()
    elif(i.islower()):
        i=i.upper()
    s1=s1+i
print("Case Toggled: ",s1)
