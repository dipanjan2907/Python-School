a=0
b=1
l1=[]
for i in range(1,10):
    l1.append(a)
    c=a
    a=b
    b=a+c
a=0
for i in range(5,0,-1):
    print(" "*(5-i),end=" ")
    for j in range(1,i+1):
        if j%2!=0:
            print(l1[a],end="")
            a+=1
        elif j%2==0:
            print("*",end="")
    print(" ")