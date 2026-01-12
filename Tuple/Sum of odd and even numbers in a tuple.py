se,so=0,0
t1=()
l=int(input("How many numbers do you want to enter?: "))
for i in range(0,l):
    n=int(input("Enter number: "))
    t1=t1+(n,)
for i in t1:
    if (i%2==0):
        se+=i
    else:
         so+=i
print("Sum of even numbers: ",se)
print("Sum of odd numbers: ",so)
