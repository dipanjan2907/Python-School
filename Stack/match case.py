st1=[]
inp=1
def isEmpty(st1):
    if(len(st1)==0):
        return True
    else:
        return False
def top(st1):
    if isEmpty(st1):
        print("UNDERFLOW")
        return None
    else:
         return st1[len(st1)-1]
def Push(st1,n):
    st1.append(n)
def Pop(st1):
    if isEmpty(st1):
        print("UNDERFLOW")
        return None
    else:
        return(st1.pop())
while(inp>0):
    print("\n0. Exit\n1. Push\n2. Display\n3. Popout\n4. Size")
    inp=int(input("Enter your choice: "))
    match(inp):
        case 0:
            print("\nBYE!")
            SystemExit
        case 1:
            n=int(input("Enter number: "))
            Push(st1,n)
        case 2:
            if isEmpty(st1):
                print("Stack UNDERFLOW","\n")
            else:
                for i in range(len(st1)-1,-1,-1):
                    print(st1[i])
        case 3:
            print("\nPopped out element= ",Pop(st1),"\n")
        case 4:
            print("\nLength= ",len(st1),"\n")
