oc=int(input("Enter Octal Number: "))
s,i=0,0
while(oc>0):
    n=oc%10
    s=s+(n*(8**i))
    i+=1
    oc//=10
print("Decimal= ",s)
sc=s
l1=[]
s1=0
while(s>0):
    l1.append(s%2)
    s//=2
l1.reverse()
for i in l1:
    s1=(s1*10)+i
print("Binary= ",s1)
l2=[]
while(sc>0):
    if(sc%16==10):
        l2.append("A")
    elif(sc%16==11):
        l2.append("B")
    elif(sc%16==12):
        l2.append("C")
    elif(sc%16==13):
        l2.append("D")
    elif(sc%16==14):
        l2.append("E")
    elif(sc%16==15):
        l2.append("F")
    else:
        l2.append(sc%16)
    sc//=16
l2.reverse()
print("Hexadecimal= ",end="")
for i in l2:
    print(i,end=" ")