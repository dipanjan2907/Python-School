l1=[]
for i in range(0,20):
    w=input("Enter string: ")
    l1.append(w)
l2=[]
for i in range(0,20):
    s=l1[i]
    s1=""
    for j in range(len(s)-1,-1,-1):
        s1+=s[j]
    l2.append(s1)
print(l2)