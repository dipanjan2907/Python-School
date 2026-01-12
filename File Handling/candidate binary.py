import pickle
def write():
    try:
        with open("candidates.dat",'ab') as f:
            while True:
                candidate_id=int(input("Enter Candidate ID: "))
                candidate_name=input("Enter Candidate Name: ").title()
                designation=input(f"Enter Designation for {candidate_name}: ").title()
                experience=float(input(f"Experience of {candidate_name}: "))
                d={'Candidate ID: ':candidate_id,'Candidate Name: ':candidate_name,'Designation: ':designation,'Experience: ':experience}
                pickle.dump(d,f)
                f1=input("----DATA INSERTED----\n||-Enter more (Y/N): ").strip()
                if f1.lower()=='n':
                    print()
                    break
    except (FileNotFoundError,EOFError,Exception) as e:
        print(f"ERROR: {e}")
def update():
        a=0
        c1=[]
        with open("candidates.dat",'rb') as f:
            while True:
                c=pickle.load(f)
                c1.append(c)
                try:
                    for i in c1:
                        if i['Experience']>10 and i['Designation']=='Manager':
                            i['Designation']='Senior Manager'
                            a+=1
                except (FileNotFoundError,EOFError,Exception) as e:
                    print(f"ERROR: {e}")
                    break
        with open("candidates.dat",'wb') as f:
            for i in c1:
                pickle.dump(i,f)
        print(a," DESIGNATIONS UPDATED..")
    
def display():
    with open("candidates.dat",'rb') as f:
            while True:
                try:
                    c=pickle.load(f)
                    if c['Designation']!='Senior Manager':
                        print(c)
                except (FileNotFoundError,EOFError,Exception) as e:
                    print(f"ERROR: {e}")    
while True:
    f2=int(input("1. Write\n2. Update\n3. DISPLAY SELECTED\nChoice: "))
    if f2==1:
        write()
    elif f2==2:
        update()    
    elif f2==3:
        display()
    else:
        break