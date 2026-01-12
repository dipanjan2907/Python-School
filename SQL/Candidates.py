import pickle
def input1():
    candidates=[]
    while True:
        cid=int(input("Enter ID: "))
        cname=input("Enter Name: ")
        des=input("Enter Designation: ")
        exp=float(input("Enter Experience: "))
        candidates.append([cid,cname,des,exp])
        ch=input("More? Y/N: ")
        if ch in 'Nn':
            break
    return candidates
clist=input1()
def append(candidates):
    with open("Candidates.dat","ab") as f:
        for i in candidates:
            pickle.dump(i,f)
    print("Success!")
append(clist)

def update():
    updated_candidates=[]
    try:
        with open("Candidates.dat",'rb') as f:
            while True:
                try:
                    d=pickle.load(f)
                    if d[3]>10:
                        d[2]='Senior Manager'
                    updated_candidates.append(d)
                except EOFError as e:
                    break
    except FileNotFoundError:
        print("No candidate data found!")
        return
    
    with open("Candidates.dat",'wb') as f:
            for i in updated_candidates:
                pickle.dump(i,f)
update()
def notseniordisplay():
    try:
        with open("Candidates.dat",'rb') as f:
            while True:
                try:
                    d=pickle.load(f)
                    if d[2]!='Senior Manager':
                        print(d)
                except EOFError as e:
                    break
    except FileNotFoundError:
        print("No candidate data found!")
        return
notseniordisplay()