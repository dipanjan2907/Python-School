l=int(input('Enter limit: '))
l1,l2,l3=[],[],[]
print("Enter numbers: ")
for i in range(0,l):
    print(i+1,end="")
    l1.append(int(input(". ")))
s=int(input("From which position to separate?: "))
l2=l1[0:s]
l3=l1[s:l]
l3.extend(l2)
print(l3)