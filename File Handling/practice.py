with open ("practice.txt","r") as file:
    ln,f=1,0
    while f==0:
        data=file.readline()
        if "learning" in data:
            print (f"Learning found first in Line Number {ln}")
            f=1
        else:
            ln+=1
with open ("practice.txt","r") as file:
    d=file.read()
    e=0
    for i in d:
        if i.isdigit():
            if (int(i))%2==0:
                e+=1
    print(f"there are {e} even numbers.")
with open ("practice.txt","r") as file:
    data=file.readline(20)
    print(data)