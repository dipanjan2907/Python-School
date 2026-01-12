t1=()
l=int(input("Enter limit: "))
for i in range(0,l):
    a=int(input("Enter number: "))
    t1=t1+(a,)
for i in range(0,l):
    print("Max: ",t1[l-1]," Min: ",t1[0])