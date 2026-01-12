l1=[]
l2=[]
flag=0
l=int(input("Enter limit {same for both the lists}: "))
for i in range(0,l):
    n=input("Enter element for List 1: ")
    l1.append(n)
for i in range(0,l):
    n=input("Enter element for List 2: ")
    l2.append(n)
for i in l1:
    for j in l2:
        if (i==j):
            flag=1
            break
if (flag==1):
    print("TRUE! At least one element common in both the lists")
else:
    print("No element common")
