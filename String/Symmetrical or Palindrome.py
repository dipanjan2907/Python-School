w=input("Enter word: ")
m=(len(w))//2
f1,f2=0,0
s1=w[0:m]
s2=w[m:len(w)]
if(s1==s2):
    f1=1
if(w==w[::-1]):
    f2=1
if(f1==1 and f2==1):
    print("Both Palindrome and Symmetrical")
elif(f1==1):
    print("Symmetrical")
elif(f2==1):
    print("Palindrome")
else:
    print("Neither Palindrome nor Symmetrical")    