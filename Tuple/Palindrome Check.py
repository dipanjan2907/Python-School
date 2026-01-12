n=int(input("Enter number: "))
def Palindrome(a):
    ac=a
    t1=()
    while a>0:
        t1=t1+((a%10),)
        a//=10
    b=0
    for i in range(0,len(t1)):
        b*=10
        b+=t1[i]
    
    if ac==b:
        print(ac," is Palindrome.")
    else:
        print(ac," is not Palindrome.")
Palindrome(n)