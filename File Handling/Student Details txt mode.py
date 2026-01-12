import pickle
s=""
with open("Student.txt", "w") as stuf:
  a='y'
  while a in ['y',"Y"]:
    roll=int(input("\nEnter roll number: "))
    name=input("Enter name: ")
    clas=int(input("Enter class: "))
    s=f"Name: {name} ; Class: {clas} ; Roll No.: {roll}\n"
    stuf.write(s)
    a=input("\nMore Data? (y/n): ")
stuf.close()
stuf=open("Student.txt","r")
d=stuf.read()
print(d)