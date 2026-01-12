n=int(input("Enter a Number: "))
se=0
so=0
while(1,10):
 n1=n%10
 if(n1%2==0):
  se+=1
 else:
  so+=1
 n=n/10
print("SUm of ODD numbers= ",so)
print("SUm of EVEN numbers= ",se)
