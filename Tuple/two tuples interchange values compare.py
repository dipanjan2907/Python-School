l=int(input("How many elements to enter {APPLIES TO BOTH THE TUPLES} ?: "))
t1=()
t2=()
print("\nEntering elements for First Tuple")
for i in range(0,l):
    n=int(input("Enter number: "))
    t1=t1+(n,)
print("\nEntering elements for Second Tuple")
for i in range(0,l):
    n=int(input("Enter number: "))
    t2=t2+(n,)
print("\nOriginal:")
print("First Tuple: ",t1)
print("Second Tuple: ",t2)
print("\nInterchanged:")
t=t1
t1=t2
t2=t
print("First Tuple: ",t1)
print("Second Tuple: ",t2,"\n")
print("Difference based on interchanged tuples")
for i in range(0,l):
    print("Element ",i+1,": ",t1[i]," - ",t2[i]," = ",t1[i]-t2[i])
