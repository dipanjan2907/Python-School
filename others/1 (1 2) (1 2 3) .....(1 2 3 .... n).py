print("(1)+(1+2)+(1+2+3)+.....(1+2+3+....+n)")
n=int(input("n= "))
s1,s2=0,0
for i in range(1,n+1):
    for j in range(1,i+1):
        s1+=j
    s2+=s1
    s1=0
print("Sum= ",s2)
