f=open("Story.txt","r")
fl=0
l1=[]
for l in f:
    l1.extend(l.replace('\n','.').split("."))
for i in l1:
    i=i.strip()
    if i.startswith("K") or i.startswith("k"):
        print(i)
        fl=1
if fl==0:
    print("NO SUCH LINES")
f.close()
