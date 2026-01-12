def sum(n):
    s=0
    n1=n
    while(n1!=0):
        r=n1%10
        n1//=10
        s+=r
    return s
n=int(input("Enter number: "))
print("Sum of digits of ",n,"= ",sum(n))
