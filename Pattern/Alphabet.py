a=b=65
for c in range(0,4):
        l=[]
        a=b
        b=a+c+1
        for k in range(a,b):
            l.append(chr(k))
        if(c%2!=0):
            l.reverse()
        for i in l:
            print (i,end=" ")
        print()