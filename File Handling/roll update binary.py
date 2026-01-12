import pickle;
def write():
    f=open('Story.dat','rb+')
    while True:
        r=int(input("Enter Roll Number: "))
        n=input("Enter Name: ")
        m=float(input("Enter Marks: "))
        d=[r,n,m]
        pickle.dump(d,f)
        c=input("Want to enter more records (Y/N):- ").strip()
        if c in 'Nn':
            print("INPUT CLOSED!")
            f.close()
            break
def read():
    f=open('Story.dat','rb')
    try:
        while True:
            l=pickle.load(f)
            print(l)
    except EOFError:
        print("END OF FILE!")
        f.close()
def update():
    try:
        with open('Story.dat', 'rb+') as f:
            temp_data = []
            found = False
            try:
                while True:
                    record = pickle.load(f) 
                    temp_data.append(record) 
            except EOFError:
                pass
            roll_to_update = int(input("Enter Roll whose Marks is to be updated: "))
            for record in temp_data:
                if record[0] == roll_to_update:
                    updated_marks = int(input("Enter Updated Marks: "))
                    record[2] = updated_marks
                    found = True
                    print("MARKS UPDATED!!")
                    break
            if not found:
                print("ROLL not found!")
            else:
                f.truncate()
                for record in temp_data:
                    pickle.dump(record, f)

    except FileNotFoundError:
        print("The file does not exist.")

o=1
while o in [1,2,3]:
    o=int(input("1. Read\n2. Write\n3. Update\nCHOICE: "))
    if o==1:
        read()
    elif o==2:
        write()
    elif o==3:
        update()
    else:
        print("Invalid Option!")