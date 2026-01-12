import pickle
stu=[]#{}
stuf=open("Student.dat","wb+")
a='y'
while a in ['y',"Y"]:
    roll=int(input("\nEnter roll number: "))
    name=input("Enter name: ")
    clas=int(input("Enter class: "))
    stu=[name,clas,roll]
    '''stu['Name: ']=name
    stu['Class: ']=clas
    stu['Roll Number: ']=roll'''
    pickle.dump(stu,stuf)
    a=input("\nMore Data? (y/n): ")
stuf.close()
stuf=open("Student.dat","rb")
sr=int(input("Enter roll number to be searched: "))
found=False
try:
    while True:
        ld=pickle.load(stuf)
        if(sr==ld[2]):
            print("Found")
            print(ld)
            found=True
except EOFError:        
    stuf.close()
if found==True:
       print("Found")
else:
       print("Not Found")
stuf=open("Student.dat","rb+")
try:
  while True:
    p=stuf.tell()
    ld=pickle.load(stuf)
    if ld[2]>2:
      ld[2]+=1
      stuf.seek(p)
      pickle.dump(ld,stuf)
except EOFError:
  pass
stuf.seek(0)
try:
    while True:
        dat=pickle.load(stuf)
        print(dat)
except:
  stuf.close()