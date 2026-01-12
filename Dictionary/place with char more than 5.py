PLACES={}
def countNow(PLACES):   
    for i in PLACES.values():
        if len(i)>5:
            print(i)
i=1
n='a'
while n.strip()!='':
    n=input("Enter Name of the Place: ")
    if n.strip()!='':
        PLACES[i]=n
        i+=1
countNow(PLACES)
