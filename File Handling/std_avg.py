import csv
def data_input():
    with open ("std_avg.csv",'w',newline='') as obj:
        f=csv.writer(obj)
        f.writerow(['Name','Maths','CS','Phy'])
        while True:
            n=input("Name: ")
            m=int(input("Maths: "))
            cs=int(input("Computer Science: "))
            p=int(input("Physics: "))
            f.writerow([n,m,cs,p])
            ch=int(input("1. More or 2. Done\n1 or 2?: "))
            if ch==2:
                break
    print("Data(s) inputted successfully.")
def avg():
    updated_data=[]
    with open ("std_avg.csv",'r') as f:
        d=csv.reader(f)
        next(f)
        for i in d:
            avrg=(int(i[1])+int(i[2])+int(i[3]))/3
            if avrg>=85:
                grade='A'            
            elif avrg>=70 and avrg<85:
                grade='B'
            elif avrg<70:
                grade='C'
            i.append(avrg)
            i.append(grade)
            updated_data.append(i)
        print("Average and Grade Added")
    with open ("std_avg.csv",'w',newline='') as obj:
        f=csv.writer(obj)
        f.writerow(['Name','Maths','CS','Phy','Average','Grade'])
        f.writerows(updated_data)
def disp():
    with open ("std_avg.csv",'r') as f:
        d=csv.reader(f)
        for i in d:
            print(i)
while True:
    ch=int(input("1. Input Data\n2. Average and Grade\n3. Display\n1/2/3?: "))
    if ch in [1,2,3]:
     if ch==1:
        data_input()
     elif ch==2:
        avg()
     elif ch==3:
        disp()
    else:
        print("!*!")
        break