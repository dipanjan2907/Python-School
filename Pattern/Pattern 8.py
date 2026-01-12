l1=['A','B','C','D','E']
c=-2
c2=1
c3=0
for i in range(5,0,-1):
    for j in range(0,i):
        print(l1[j],end=" ")
    for l in range(1,c2):
        print("",end=" ")
    c3=j
    c2+=3
    if(i<5):
        print(l1[c3],end=" ")
    for k in range(c,-6,-1):
        print(l1[k],end=" ")
    c-=1
    print(" ")
