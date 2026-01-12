l=int(input("How many numbers do you want to input:"))
list1=[]
for i in range(1,l+1):
    n=int(input("Enter number: "))
    list1.append(n)
list2=list(set(list1))
list2.sort()
print("Second largest element is:", list2[-2])
