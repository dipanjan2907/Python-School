n=int(input("Enter number: "))
flag=0
while n>0:
    r=n%10
    n=n//10
    if r==0:
        flag=1
if flag==1:
    print("DUCK number")
else:
    print("NOT DUCK number.")
    
