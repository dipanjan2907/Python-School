import csv
def write():
    f=open('CSVFILE.csv','a')
    wo=csv.writer(f)
    wo.writerow(['userid','password'])
    while True:
        uid=input("Enter User ID: ")
        pswd=input("Enter Password: ")
        data=[uid,pswd]
        wo.writerow(data)
        c=input("Want to enter more data (Y/N): ")
        if c in 'Nn':
            break
    f.close()
def read():
    f=open('CSVFILE.csv','r')
    ro=csv.reader(f)
    for i in ro:
        print(i)
    f.close()
def search():   
    f=open('CSVFILE.csv','r')
    found=0
    u=input("Enter USER ID to be Searched: ")
    ro=csv.reader(f)
    for i in ro:
        if i[0]==u:
            print("PASSWORD: ",i[1])
            found=1
    if found==0:
        print("RECORD NOT FOUND!")
    f.close()
ch=1
while ch in [1,2,3]:
    ch=int(input("1. WRITE\n2. READ\n3. SEARCH\nENTER CHOICE{1/2/3}: "))
    if ch==1:
        write()
    elif ch==2:
        read()
    elif ch==3:
        search()
    else:
        print("EXITTED!")