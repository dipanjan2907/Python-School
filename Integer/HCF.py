a=int(input("Enter 1st no."))
b=int(input("Enter 2nd no."))
if a>b:
    l=a
else:
    l=b
for i in range(l+1,0,-1):
 if a%i==0 and b%i==0:
  print ("HCF=",i)
  break
print("LCM=",(a*b)//i)
