L2=[]
def Push_Element(NList):
    l1=[]
    c=input("City: ")
    y=input("Country: ")
    d=int(input("Distance from Delhi(km): "))
    if (y not in ["India"] and d<3500):
        l1.append(c)
        l1.append(y)
        NList.append(l1)
def Pop_Element(NList):
    while len(NList)>0:
        o=NList.pop()
        print(o,end=" , ")
    print("Stack Empty.")
L=int(input("Limit: "))
for i in range(1,L+1):
    Push_Element(L2)
Pop_Element(L2)
