print("Enter numbers one by one by pressing enter\nnon-number stops input")
i=1
l=[]
while True:
    n=input("-> ")
    if n.isdigit():
        l.append(n)
    else:
        print("You didn't enter a number...INPUT CLOSED")
        break
print("Original: ",l)
l[0],l[len(l)-1]=l[len(l)-1],l[0]
print("First and last number interchanged: ",l)