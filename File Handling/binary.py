import pickle
def input1():
    with open("binary.dat","wb") as f:
        while True:
            r=int(input("Student Roll No.: "))
            n=input("Student Name: ")
            m=int(input("Enter Marks: "))
            data={'Roll: ':r, 'Name: ':n, 'Marks: ':m}
            pickle.dump(data,f)
            ch=int(input("\nData Entered Successfully!\n1. Continue Data Entry\n2. Exit\n1 or 2?: "))
            if ch==2:
                break
    print("Data Entry Closed.")

def search():
    s=int(input("Enter Roll Number to Search: "))
    flag=0
    with open("binary.dat","rb") as f:
        try:
            while True:
                data=pickle.load(f)
                if data['Roll: ']==s:
                    print("Found...")
                    print(data)
                    f=1
                    break
        except EOFError:
            if flag==0:
                print(f"Roll No {s} NOT Found!!")
            print()

def update_marks():
    flag=0
    listdata=[]
    s=int(input("Enter Roll whose marks is to be updated: "))
    newm=int(input(f"Enter New Marks for Roll {s}: "))
    try:
        with open("binary.dat","rb") as f:
            while True:
                data=pickle.load(f)
                listdata.append(data)
    except EOFError:
        print()
    
    for i in listdata:
        if i['Roll: ']==s:
            i['Marks: ']=newm
            print("Marks Updated!")
            flag=1
    with open("binary.dat","wb+") as f:
        for i in listdata:
            pickle.dump(i,f)
    if flag==0:
        print("Roll Number Not Found!")

def display():
    try:
        with open("binary.dat","rb") as f:
            while True:
                data=pickle.load(f)
                print(data)
    except EOFError:
        print()

#input1() 
#search()
#update_marks()
display()
