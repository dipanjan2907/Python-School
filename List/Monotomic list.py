l=int(input('Enter limit: '))
l1=[]
f=0
print("Enter numbers: ")
for i in range(0,l):
    print(i+1,end="")
    l1.append(int(input(". ")))
if(l1[0]<=l1[1]):
    f1=1
elif(l1[0]>=l1[1]):
    f1=2
for i in range(1,l):
    if(f1==1 and (l1[i-1]<=l1[i])):
        f=1
    elif(f1==2 and (l1[i-1]>=l1[i])):
        f=1
    else:
        f=0
        break
if(f==1):
    print("Monotonic")
else:
    print("Not Monotonic")