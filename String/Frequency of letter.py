s=input("Enter a sentence or word: ")
t1=()
c=0
f=dict()
for i in range(0,len(s)):
    t1+=(s[i],)
for i in t1:
    for j in t1:
        if(i==j):
            c+=1
            f[i]=c
    c=0
print("\nLetter\t:\tNumber of times present")
for i in f:
    print(" ",end="")
    if (i==' '):
        print("Space\t:\t",f[i])
    else:
        print(i,"\t:\t",f[i])
