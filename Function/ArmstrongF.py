num=int(input("Enter number: "))
def Armstrong(n):
    s=0
    n1=n
    while(n!=0):
        s=s+((n%10)**3)
        n//=10
    if(n1==s):
        return True
    else:
        return False
if Armstrong(num):
    print(num," is Armstrong.")
else:
    print(num," is not Armstrong")