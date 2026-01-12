n1=int(input("Enter number: "))
n2=int(input("Enter number: "))
for i in range(1,n1+1):
    if (n1%i==0 and n2%i==0):
        g=i
print("GCD= ",g)
print("LCM= ",n1*n2//g)
#for i in range(1,n1+1):
#   if (n1%n2==0):
#       print("LCM= ",n1)
#       break
#   elif(n2%n1==0):
#       print("LCM= ",n2)
#       break
#   else:
#       print("LCM= ",n1*n2)
#       break
