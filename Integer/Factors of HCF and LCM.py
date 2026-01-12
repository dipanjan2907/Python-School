a=int(input("Enter 1st no: "))
b=int(input("Enter 2nd no: "))
if a>b:
    l=a
else:
    l=b
for i in range(1,l+1):
 if a%i==0 and b%i==0:
     HCF=i
LCM=(a*b)//HCF
print("HCF= ",HCF)
print("LCM=",LCM)
print("\nFactors of HCF")
for i in range(1,HCF+1):
    if(HCF%i==0):
        print(i,"*",HCF//i," = ",HCF)
print("\nFactors of LCM")
for i in range(1,LCM+1):
    if(LCM%i==0):
        print(i,"*",LCM//i," = ",LCM)
