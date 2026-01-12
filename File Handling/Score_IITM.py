import csv
A,B,C=0,0,0
l1=[]
with open("Score_IITM.csv") as f:
    r=csv.reader(f)
    for i in r:
        l1.extend(i)
    for i in l1:
        if int(i)>250:
            A+=1
        elif int(i)>200 and int(i)<250:
            B+=1
        elif int(i)<200:
            C+=1
print(f"A={A}\nB={B}\nC={C}")