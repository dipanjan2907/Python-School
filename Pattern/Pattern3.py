s,e=1,10
for i in range(1,6):
    for j in range(s,e):
        print(j,end=" ")
    s,e=s+1,e-1
    print(" ")
