s=input("Enter name: ")
for i in range(len(s)-1,0,-1):
    if s[i]==" ":
        sn=s[i+1:]+" "+s[0:i]
print(sn)   
        
