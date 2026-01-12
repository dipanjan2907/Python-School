N=[10, 5, 8, 3, 12]
EvenNumbers=[]
l=int(input("How many?: "))
for i in range(0,l):
    N.append(int(input("Number: ")))
def push_even(N,EvenNumbers):
    for i in N:
        if i%2==0:
            EvenNumbers.append(i)
def pop_even(EvenNumbers):
    if len(EvenNumbers)==0:
        print("Empty..")
    else:
        return EvenNumbers.pop()
def Disp_even(EvenNumbers):
    if len(EvenNumbers)==0:
        print("None..")
    else:
        print("Even Numbers: ")
        for i in range(len(EvenNumbers)-1,-1,-1):
            print(EvenNumbers[i],end=",")
push_even(N,EvenNumbers)
Disp_even(EvenNumbers)
print("\nPopped Number: ",pop_even(EvenNumbers))