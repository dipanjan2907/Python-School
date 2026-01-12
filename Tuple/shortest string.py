t1=()
n=int(input("Limit: "))
if(n>0):
    for i in range(0,n):    
        a=input("Enter word: ")
        t1=t1+(a,)
    c=len(t1[0])
    for i in range(1,len(t1)):
        a=len(t1[i])
        if(a<c):
            c=a
    print("Length of shortest string: ",c)
else:
    print("TUPLE CAN'T BE EMPTY!")