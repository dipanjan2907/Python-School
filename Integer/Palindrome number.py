try:
    n=int(input("Enter number: "))
    n1=n
    n2=0
    
    while(n1>0):
        n2=n2*10+(n1%10)
        n1//=10
    if (n2==n):
        print(n," is a Palindrome number")
    elif n2!=n:
        print(n," is not a Palindrome number")
except ValueError as e:
    print(f"Invalid Input: {e}")