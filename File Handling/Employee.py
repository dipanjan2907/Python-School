#Saves employee records (ID, Name, Salary) in a binary file.
#Reads the file and displays all employees earning more than ₹50,000.
#Deletes a record of a specific employee and rewrites the file.
import pickle
def input1():
    with open("employee.dat","ab") as f:
        duplicatecheck=[]
        while True:
          id=int(input("Enter Employee ID: "))
          if id not in duplicatecheck:
            duplicatecheck.append(id)
            n=input("Enter Employee Name: ")
            s=int(input("Enter Employee Salary: "))
            d={'ID: ':id,'Name: ':n,'Salary: ':s}
            pickle.dump(d,f)
            ch=int(input("1. Continue\n2. Stop\n1 or 2: "))
            if ch==2:
                break
          else:
              print("**ID's NEED TO BE UNIQUE**")

def filtered():
  with open("employee.dat","rb") as f:
    try:
        while True:
            data=pickle.load(f)
            if data['Salary: ']>50000:
                print(data)
    except EOFError:
        print()

def delete():
    d1=[]
    d=int(input("Enter Employee ID to delete: "))
    with open("employee.dat","rb") as f:
        try:
            while True:
                data=pickle.load(f)
                if data['ID: ']!=d:
                    d1.append(data)
                else:
                    print(f"Employee with {d} deleted.")
        except EOFError:
            print()
        #f.seek(0)
        #f.flush()
    with open("employee.dat","wb") as f:
        for i in d1:
            pickle.dump(i,f)
def display():
    with open("employee.dat","rb") as f:
        try:
            while True:
                data=pickle.load(f)
                if data:
                    print(data)
                else:
                    break
        except EOFError:
            print()
while True:
    print("1. Input Details\n2. Display Employee Name whose Salary above 50K")
    print("3. Delete Employee by ID\n4. Display All\n5. Delete All")
    ch=int(input("1/2/3/4/5: "))
    if ch in [1,2,3,4,5]:
        if ch==1:
            input1()
        elif ch==2:
            filtered()
        elif ch==3:
            delete()
        elif ch==4:
            display()
        elif ch==5:
            with open("employee.dat","wb") as f:
                f.seek(0)
                f.flush()
            print("Deleted")
    else:
        print("Invalid Input")
        break