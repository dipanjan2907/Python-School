import mysql.connector as sqltor
con=sqltor.connect(host="localhost",
                   user="group",
                   password="G#n6Hg59",
                   database="SchoolDB")
if con.is_connected():
    print("Connected!")
    cursor=con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Students(StudentID INT PRIMARY KEY,Name VARCHAR(100),Age INT, Grade VARCHAR(10))")
    print(".....✔️")
    def insert():
        while True:
            s=int(input("\nEnter Student ID: "))
            n=input("Enter Student Name: ")
            a=int(input("Enter Student Age: "))
            g=input("Enter Student Grade: ")
            cursor.execute("INSERT INTO Students(StudentID,Name,Age,Grade) VALUES (%s,%s,%s,%s)",(s,n,a,g))
            con.commit()
            ch=input("*✔️*\nWant to input more data? (y/n: ")
            if ch in 'Nn':
                break
    def display():
        cursor.execute("SELECT * FROM Students")
        result=cursor.fetchall()
        print(f"{'StudentID':<25}{'Name':<150}{'Age':<20}{'Grade':<10}")
        for i in result:
            print(f"{i[0]:<25}{i[1]:<150}{i[2]:<20}{i[3]:<10}")
    while True:
        ch=int(input("1. INSERT\n2. DISPLAY\n3. EXIT\n1/2/3: "))
        if ch==1:
            insert()
        elif ch==2:
            display()
        else:
            print("Exitting...\n✔️")
            cursor.close()
            con.close()
            break
else:   
    print("❌❌-CONNECTION UNSUCCESSFUL-❌❌")

