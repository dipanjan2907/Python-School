def push(stk,val):
    stk.append(val)
    print("PUSHED SUCCESSFULLY.")
def popitem(stk):
    print("Deleted Value= ",stk.pop())
def peep(stk):
    print("Peeped Element= ",len(stk)-1)
def display(stk):
    for i in range(len(stk)-1,-1,-1):
        print(stk[i])
stk=[]
while True:
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Peep")
    print("5. Exit")
    ch=int(input("Enter the choice: "))
    if ch==1:
        val=int(input("Enter the value: "))
        push(stk,val)
    elif ch==2:
        if len(stk)==0:
            print("Empty Stack.")
        else:
            popitem(stk)
    elif ch==3:
        if len(stk)==0:
            print("Empty Stack.")
        else:
            display(stk)
    elif ch==4:
        if len(stk)==0:
            print("Empty Stack.")
        else:
            peep(stk)
    else:
        break