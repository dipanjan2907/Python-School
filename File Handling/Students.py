f=open("Marks.txt","w+")
l=int(input("Limit: "))
for i in range(1,l+1):
    r=int(input("Roll: "))
    n=input("Name: ")
    m=float(input("Marks: "))
    rec="Roll: "+str(r)+"\nName: "+n+"\nMarks: "+str(m)+"\n\n"
    f.write(rec)
print("\n\n")
f=open("Marks.txt","r")
while l:
    print(l)
    l=f.read()
f.close()