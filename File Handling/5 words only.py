f=open("Story.txt","r")
for l in f:
    w=l.split()
    if(len(w)==5):
        print(l.strip())
f.close()

'''we wander through paths unknown.
casting light on endless possibilities.
Others are boundless, without end.
Each day brings new beginnings,
Courage sometimes means moving forward,
Love finds its way, always.'''