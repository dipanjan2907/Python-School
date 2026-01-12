n=int(input("Enter the value of n: "))
def Mersenne(a):
    l1=[]
    for i in range(1,a+1):
        l1.append((2**i)-1)
    return l1
print(Mersenne(n))
print(Mersenne(n**n))