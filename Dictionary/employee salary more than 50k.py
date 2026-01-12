d={}
i=1
while True:
    n=input("Enter Employee Name: ")
    s=int(input("Enter Employee Salary: "))
    d[i]=(n,s)
    c=input("Do you want to add more records? (y/n): ")
    if c.lower()=='n':
        break
    else:
        i+=1
def highSalary(d):
    for i in d.values():
        if i[1]>50000:
            print(i[0])
highSalary(d)