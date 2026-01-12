l=int(input("How many magic numbers to show?: "))
i=1
n=10
while i<=l:
    s=10
    a=n
    while s>9:
        s=0
        while a>0:
            s+=(a%10)
            a//=10
        a=s
    if s==1:
        print(n)
        i+=1

    n+=1
