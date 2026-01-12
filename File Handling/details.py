import csv
with open("detail.csv","w",newline="") as obj:
    f=csv.writer(obj)
    f.writerow(['Name','Roll','Total'])
    while True:
        r=int(input("Enter Roll: "))
        n=input("Enter Name: ")
        t=int(input("Enter Total Marks: "))
        f.writerow([n,r,t])
        ch=int(input("1. Enter More\n2. Exit\n1 or 2?: "))
        if ch==2:
            break

with open("detail.csv","r") as obj:
    print("\nStudents with marks greater than 75:")
    f=csv.reader(obj)
    next(f)
    for i in f:
        if int(i[2])>75:
            print(f"{i[0]}, who hold Roll Number {i[1]}, scored {i[2]} marks.")

with open("detail.csv","r") as obj:
    fl=0
    s=int(input("\nEnter Roll No. to search: "))
    f=csv.reader(obj)
    next(f)
    for i in f:
        if int(i[1])==s:
            fl=1
            break
    if fl==0:
        print(f"Roll Number {s} not found.")
    else:
        print(f"Roll Number {s} found.")
with open("detail.csv","r") as obj:
    f=csv.reader(obj)
    next(f)
    max=0
    for i in f:
        if int(i[2])>max:
            max=int(i[2])
            max_details=f"\n{i[0]}, who hold Roll Number {i[1]}, scored {i[2]}, the Maximum Marks."
    print(max_details)