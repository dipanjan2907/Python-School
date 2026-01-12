import pickle
c=int(input("1.Input Data\n2. Display\n3. Search for Marks\nChoice: "))
if c==1:
    f=open("file.dat","ab+")
    l=int(input("How many?: "))
    for i in range(0,l):
        r=int(input("Enter Roll: "))
        n=input("Enter student name: ")
        m=int(input("Enter Marks: "))
        a={'ROLL: ':r, 'NAME: ':n,'MARKS: ':m}
        pickle.dump(a,f)
    f.close()
elif c==2:
    f=open("file.dat",'rb')
    while True:
        try:
            print("DATA:\n",pickle.load(f))
        except EOFError:
            break
    f.close()
elif c==3:
    f=open("file.dat",'rb')
    found=False
    s=int(input("Enter Roll to search: "))
    while True:
        try:
            me=pickle.load(f)
            if me['ROLL: ']==s:
                print("|----------FOUND----------|")
                found=True
                print("ROLL: ",me['ROLL: '],"\nNAME: ",me['NAME: '],"\nMARKS: ",me['MARKS: '])
        except EOFError:
            break
    if found==False:
            print("NOT FOUND")
    f.close()
elif c == 4:
    s = int(input("Enter Roll to update marks: "))
    updated = False
    records = []
    try:
        with open("file.dat", 'rb') as f:
            while True:
                records.append(pickle.load(f))
    except EOFError:
        pass
    for record in records:
        if record['ROLL: '] == s:
            print("Current Marks: ", record['MARKS: '])
            new_marks = int(input("Enter new marks: "))
            record['MARKS: '] = new_marks
            updated = True
            print("Marks updated successfully!")
    with open("file.dat", 'wb') as f:
        for record in records:
            pickle.dump(record, f)
    if not updated:
        print("Roll number not found.")
f.close()