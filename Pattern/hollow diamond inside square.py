a=int(input("ENTER LENGTH (even): "))
print("*"*a)
b=(a//2)-1
c=b//2
for i in range(1,a//2):
    print("*"*b + " "*c + "*"*b) 
    b-=1
    c+=2
b=1
c=a-2
for i in range(1,a//2):
    print("*"*b + " "*c + "*"*b)
    b+=1
    c-=2
