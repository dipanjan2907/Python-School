x=int(input("Enter number: "))
n=int(input("Enter limit: "))
p=1
for i in range(1,n+1,+2):
        p=p*(x+i)    
print(p)
