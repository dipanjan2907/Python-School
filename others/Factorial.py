def Factorial(a):#function definition(formal parameter))
    f=1
    for i in range(1,a+1):
        f*=i
    return f
#main
n=int(input("Enter number: "))
print(Factorial(n))#actual parameter(function calling)