a=int(input("ENTER LENGTH (even): "))
if(a%2==0):
    b=a//2
    for i in range(1,a//2+1):
        print(" "*b+"*"*b)
    for i in range(a//2,a+1):
        print("*"*b+" "*b)
else:
    print("STUDY MATHS FIRST! You think ",a," is EVEN?? XD")