se,so=0,0
listn=[1,2,3,4,5,6,7,8,9,10];
listo=[];
liste=[];
for i in listn:
    if i%2==0:
        liste.append(i);
        se+=i
    else:
        listo.append(i);
        so+=i
print("ODD NUMBERS\n",listo,"\nSum of odd numbers= ",so)
print("EVEN NUMBERS\n",liste,"\nSum of even numbers= ",se)

    
