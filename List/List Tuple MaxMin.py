l=int(input("How many elements to enter?: "))
l1=[]
for i in range(0,l):
    n=int(input("Enter the numbers: "))
    l1.append(n)
t1=()
for i in l1:
    t1=t1+(i,)
print("Numbers you entered- ",t1)
print("Maximum value: ",max(t1))
print("Minimum value: ",min(t1))
