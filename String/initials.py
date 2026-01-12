s=input("Enter name: ")
s=" "+s
sn=" "
for i in range(0,len(s)):
    if s[i]==" ":
        sn=sn+s[i+1]+"."
print("Initials: ",sn)
