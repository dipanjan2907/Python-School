import mysql.connector as sqltor
try:
    con=sqltor.connect(host="localhost",
                   user="group",
                   password="G#n6Hg59",
                   database="ITEMDB")
    if con.is_connected():
        print("CONNECTED")
        cursor=con.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS STATIONERY(ITEMNO INT(11) PRIMARY KEY,ITEMNAME VARCHAR(15),PRICE FLOAT,QTY INT(11))")
        def AddAndDisplay():
            while True:
                ino=int(input("Item Number: "))
                ina=input("Item Name: ")
                p=float(input("Price: "))
                q=int(input("Quantity: "))
                cursor.execute("INSERT INTO STATIONERY(ITEMNO,ITEMNAME,PRICE,QTY)VALUES(%s,%s,%s,%s)",(ino,ina,p,q))
                con.commit()
                ch=input("MORE? Y/N: ")
                if ch in'Nn':
                    break
            cursor.execute("SELECT * FROM STATIONERY WHERE PRICE >120")
            r=cursor.fetchall()
            print(f"{'ITEMNO':<11}{'ITEMNAME':<15}{'PRICE':<10}{'QUANTITY':<11}")
            for i in r:
                print(f"{i[0]:<11}{i[1]:<15}{i[2]:<10}{i[3]:<11}") 
        AddAndDisplay()
except sqltor.Error as e:
    print(f"Error: {e}")
finally:
    if con.is_connected():
        cursor.close()
        con.close()