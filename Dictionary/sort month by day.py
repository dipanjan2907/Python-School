d={29:'February',30:['September','April','June','November'],31:['January','March','May','July','August','October','December']}
d1={}
l2=[]
l2.append([d[29]])
for i in d.keys():
    l1=[]
    if i!=29:
        for j in d[i]:
            l1.append(j)
        l1.sort()
    l2.append(l1)
print(l2)
for i in range(0,len(l2)):
    for j in range(0,len(l2[i])):
        if i==0:
            d1[l2[i][j]]=29
        elif i==2:
            d1[l2[i][j]]=30
        elif i==3:
            d1[l2[i][j]]=31
print (d1)