def check_prime(A):
    c=0
    for i in range(1,A//2+1):
        if(A%i==0):
            c+=1
    if c==2:
        return True
    else:
        return False
def twist(B):
    l1=[]
    while(B>0):
        l1.append(B%10)
        B//=10
    n=0
    for i in l1:
        n*=10
        n+=i
    if check_prime(n):
        return True
    else:
        return False
num=int(input("Enter number: "))

if(check_prime(num) and twist(num)):
    print("TWISTED PRIME!")
elif(check_prime(num)):
    print("NOT TWISTED PRIME!")
else:
    print("NOT PRIME!")