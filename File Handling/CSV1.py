import csv
n=int(input("Enter number of entries: "))
with open("CSV1_Text_File.csv", "w", newline='') as empdata:
    writer = csv.writer(empdata)
    writer.writerow(["ID","Name","Salary"])
    for i in range(1, n+1):
        empid = int(input("\nEnter ID: "))
        empname = input("Enter name: ")
        empsalary = int(input("Enter salary: "))
        empinfo = [empid, empname, empsalary]
        writer.writerow(empinfo)