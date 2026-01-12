n=int(input("Enter number: "))
for i in range(2,n+1):
    l1=[]
    c=0
    c1=0
    for j in range(1,i+1):
        if(i%j==0):
            c+=1
    if(c==2):
        for k in range(1,n-i+1):
            if((n-i)%k==0):
                c1+=1
        if(c1==2):
            print(i," + ",n-i," = ",n)
        