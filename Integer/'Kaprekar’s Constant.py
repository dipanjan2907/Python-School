'''Kaprekar’s Constant (6174 Mystery)u
For any 4-digit number (not all digits same), if you repeatedly: 
Arrange digits in descending and ascending order. Subtract the smaller from the larger.'''
import random
diff,s=0,0
l1=[1111,2222,3333,4444,5555,6666,7777,8888,9999]
n=random.randint(1000,9999)
print(f"Randomly Generated Number: {n}")
diff=0
if n not in l1:
  while diff!=6174:
    l2=[]
    n1=n
    while n1!=0:
        l2.append(n1%10)
        n1//=10
    l3=sorted(l2)
    l4=sorted(l2,reverse=True)
    a=l3[0]*(10**3)+l3[1]*(10**2)+l3[2]*(10)+l3[3]
    b=l4[0]*(10**3)+l4[1]*(10**2)+l4[2]*(10)+l4[3]
    diff=b-a
    print(f"{b}-{a}={diff}")
    n=diff    
    s+=1
    
print(f"Kaprekar’s Constant (6174) reached in {s} steps..")
