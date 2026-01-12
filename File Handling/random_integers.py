import random
import pickle
def numbergen():
    with open("random_integers.dat","wb") as f:
        for i in range(3):
            n=random.randint(10,99)
            pickle.dump(n,f)
def display():
    with open("random_integers.dat","rb") as f:
        try:
            while True:
                data=pickle.load(f)
                if not data:
                    break
                print(data,end=", ")
        except EOFError:
            print()
def operations():
    g,s,count=0,0,0
    with open("random_integers.dat","rb") as f:
        l=pickle.load(f)
        try:
            f.seek(0)
            while True:
                data=pickle.load(f)
                if not data:
                    break
                else:
                    if g<data:
                        g=data
                    if l>data:
                        l=data
                    s+=data
                    count+=1
        except EOFError:
            print(f"Highest= {g}\nLowest= {l}\nSum= {s}\nAverage= {s/count}")
            
numbergen()
display()
operations()