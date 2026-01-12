import csv
def write():
    f=open('Happiness.csv','a',newline='')
    w=csv.writer(f)
    while True:
        c=input("Enter Country Name: ")
        p=int(input(f"Enter Population of {c}: "))
        s=int(input("Number of people who participated in the contest: "))
        h=int(input("Number of people who accepted that they are Happy: "))
        w.writerow([c,p,s,h])
        f1=input("DATA ENTERED\nEnter more (Y/N): ").strip()
        if f1.lower()=='n':
            print()
            break
    f.close()
def read():
    f=open('Happiness.csv','r')
    r=csv.reader(f,delimiter='|')
    print("Records where Population is more than 5000000-")
    for i in r:
        if len(i)==4:
            if int(i[1])>5000000:
                print(i)
    f.close()
def count():
    f=open('Happiness.csv','r')
    r=csv.reader(f)
    c=0
    for i in r:
        c+=1
    print("Number of Records: ",c)
    f.close()
while True:
    f2=int(input("1. Write into CSV\n2. Read from CSV\n3. Count no. of data in CSV\n0.Exit\nChoice: "))
    if f2==1:
        write()
    elif f2==2:
        read()
    elif f2==3:
        count()
    elif f2==0:
        break