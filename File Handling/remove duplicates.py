f=open('story.txt','r')
d=f.read()
w=d.split()
l1=[]
for i in w:
    if i.endswith('m'):
        l1.append(i)
f.close()
if len(l1)>0:
    for i in l1:
        print(i)

else:
    print("No such words")