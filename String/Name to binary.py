ch=int(input("1. Digit to Binary\n2.Name/String to Binary\nEnter choice: "))
f=0
if(ch==1):
    n=int(input("Enter number: "))
    l1=[]
    while n>0:
        l1.append(n%10)
        n//=10
    l1.reverse()
    f=1
elif(ch==2):
    n=input("Enter name/string: ")
    l1=list(n)
    f=1
else:
    print("INVALID CHOICE")
if(f==1):
    for i in range(0,len(l1)):
        c=0
        binary=0
        b=[]
        ascii=ord(l1[i])
        while(ascii>0):
            b.append(ascii%2)
            ascii//=2
        b.reverse()
        for i in b:
            binary+=i
            binary*=10
        print (binary//10,end=" ")
