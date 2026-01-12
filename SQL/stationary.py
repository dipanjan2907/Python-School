import mysql.connector as sqltor
con=sqltor.connect(
    host='localhost',
    user='root',
    password='Password@MySQL1',
    database='practice'
)
if con.is_connected():
    print("|---CONNECTED---|")
    cursor=con.cursor()
    #cursor.execute("CREATE TABLE STATIONARY (itemno INT(11) PRIMARY KEY, itemname VARCHAR(15),price FLOAT, qty INT(11))")
    print("Table Exists..")
    def AddAndDisplay():
        try:
            while True:
                ino=int(input("Enter Item Number: "))
                ina=input("Enter Item Name: ")
                p=float(input(f"Enter Price of {ina}: "))
                q=int(input(f"Quantity for {ina}: "))
                cursor.execute("INSERT INTO STATIONARY (itemno,itemname,price,qty) VALUES(%s,%s,%s,%s)",(ino,ina,p,q))
                con.commit()
                ch=input("DATA INSERTED\nWant to add more? (y/n): ").lower()
                if ch=='n':
                    break
            cursor.execute("SELECT * FROM STATIONARY WHERE PRICE>120")
            r=cursor.fetchall()
            print(f"{'ItemNo':<11} {'ItemName':<15} {'Price':<10} {'Quantity':<11}")
            for i in r:
                print(f"{i[0]:<11} {i[1]:<15} {i[2]:<10} {i[3]:<11}")
        except sqltor.Error as e:
            print(f"Error: {e}")
    AddAndDisplay()
else:
    print("Connection Failed!")