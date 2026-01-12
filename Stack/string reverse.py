def push(stk,str):
    for i in str:
        stk.append(i)
def pop(stk):
    while stk:
        d=stk.pop()
        print(d,end="")

s=input("Enter String: ")
stk=[]
push(stk,s)
pop(stk)
