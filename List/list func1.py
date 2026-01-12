l=[]
n=int(input("How many elements to enter?: "))
print("Enter elements: ")
for i in range(0,n):
    e=input(str(i+1)+"-> ")
    l.append(e)
print("Elements you entered: ",l)
p=int(input("Which position element you want to delete?: "))-1
l1=l
l1.pop(p)
l2=l
print("Postion ",p+1," element deleted: ",l1)
r=str(input("Which element to delete?: "))
l2.remove(r)
print("Element ",r," deleted: ",l2)