def isEmpty(glassStack):
    if len(glassStack)==0:
        return True
    else:
        return False
def opPush(glassStack,element):
    glassStack.append(element)
def size(glassStack):
    return len(glassStack)
def top(glassStack):
    if isEmpty(glassStack):
        print('Stack is empty')
        return None
    else:
        x =len(glassStack)
        element=glassStack[x-1]
        return element
def opPop(glassStack):
    if isEmpty(glassStack):
        print('underflow')
        return None
    else:
        return(glassStack.pop()) 
def display(glassStack):
    x=len(glassStack)
    print("Current elements in the stack are: ")
    for i in range(x-1,-1,-1):
        print(glassStack[i])
glassStack = list()
element='glass1'
print("Pushing element ",element)
opPush(glassStack,element)
element='glass2'
print("Pushing element ",element)
opPush(glassStack,element)
print("Current number of elements in stack is",size(glassStack))
element=opPop(glassStack)
print("Popped element is",element)
element='glass3'
print("Pushing element ",element)
opPush(glassStack,element)
print("top element is",top(glassStack))
display(glassStack)
while True:
    item=opPop(glassStack)
    if item == None:
        print("Stack is empty now")
        break
    else:
        print("Popped element is",item)