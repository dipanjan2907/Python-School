def push(stk,str,s):
    for i in s:
        stk.append(i)
        str.append(i)
def pop(stk,str):
    j=0
    done=False
    while len(stk)>0 and not(done):
        ch=stk.pop()
        if str[j]==ch:
            j+=1
        else:
            done=True
    if done==True:
        print("Not Palindrome")
    else:
        print("Palindrome")
s=input("Enter String: ")
stk,str=[],[]
push(stk,str,s)
pop(stk,str)