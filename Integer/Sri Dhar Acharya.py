import math
def findRoots(a, b, c):
    discriminant = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(discriminant))
    if discriminant > 0:
        print("Real Roots")
        print((-b + sqrt_val) / (2 * a))
        print((-b - sqrt_val) / (2 * a))
    elif discriminant == 0:
        print("Real and Same Roots")
        print(-b / (2 * a))
    else:
        print("Complex Roots")
        print(- b / (2 * a), "+ i", sqrt_val)
        print(- b / (2 * a), "- i", sqrt_val)
print("The equation is in the form ax^2 + bx + c = 0")
print("The Equation is : ",end=" ")
a=int(input("(x^2)"))
print("The Equation is : ",a,"x^2 + ",end=" ")
b=int(input("x"))
print("The Equation is : ",a,"x^2 + ",b,"x + ",end=" ")
c=int(input(""))                 
print("The Equation is : ",a,"x^2 + ",b,"x + ",c," = 0")
findRoots(a, b, c)