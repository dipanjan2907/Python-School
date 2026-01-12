l=[]
for i in range(97,123):
    s=""
    for j in range(97,i+1):
        s+=chr(i)
    l.append(s)
print(l)