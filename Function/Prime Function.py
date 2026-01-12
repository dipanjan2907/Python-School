num=int(input("Enter number: "))
def prime(n):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c+=1
    if(c==2):
        return True
    else:
        return False
if prime(num):
    print(num," is Prime.")
else:
    print(num," is not Prime.")