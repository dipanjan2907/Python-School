a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
print("1. Add")
print("2. Substract")
print("3. Multiply")
print("4. Divide")
opt=int(input("Enter your choice (1/2/3/4): "))
if(opt==1):
 print(a," + ",b," = ",a+b)
elif(opt==2):
    if a==b:
        print("0")
    else:
        print(a," - ",b," = ",a-b)
        print(b," - ",a," = ",b-a)
elif(opt==3):
 print(a," * ",b," = ",a*b)
elif(opt==4):
 print(a," / ",b," = ",a/b)
else:
 print("INVALID INPUT")
