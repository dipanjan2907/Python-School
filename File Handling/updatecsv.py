import csv
def write():
    with open("updatecsv.csv",'w',newline='') as obj:
        f=csv.writer(obj)
        f.writerow(['Name','Phone'])
        while True:
            n=input("Name: ")
            p=int(input("Phone Number: "))
            f.writerow([n,p])
            ch=input("More? Y/N?: ")
            if ch in 'Nn':
                break
def update():
    with open("updatecsv.csv",'r') as obj:
        fl=0
        updated=[]
        f=csv.reader(obj)
        next(f)
        n=input("Name whose Ph No. is to be updated: ")
        for i in f:
            if n==i[0]:
                ph=int(input("Enter new phone number: "))
                i[1]=ph
                fl=1
            updated.append([i[0],i[1]])
        return fl,updated
[a,b]=update()
if a==1:
    with open("updatecsv.csv",'w',newline='') as obj:
        obj.truncate(0)
        f=csv.writer(obj)
        f.writerow(['Name','Phone'])
        for i in b:
            f.writerow(i)
    with open("updatecsv.csv",'r') as obj:
        f=csv.reader(obj)
        for i in f:
            print(i)
else:
    print("Name not found.")

