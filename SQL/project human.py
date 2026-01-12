# 1. make and enter data into table CUSTOMER (Name, contact, address) and perform operations
# 2. make and enter data into table products (P_ID,Name,Specs, stock, price) and perform operations
# 3. make and enter data into table SALES (cname, prod id, quantity sold) and perform operations
# OPERATIONS ON:  a) Customers- add, update delete,view b) products add, update delete,view c) Sales: make and view sales
import mysql.connector as sqltor
con = sqltor.connect(
    host="localhost",
    user="group",
    password="G#n6Hg59",
    database="Computer_Sales_System"
)
if con.is_connected():
    print("||-------->>Connection successfully established<<--------||\n")
    print("<>-<>-<>-Welcome to Computer and Accessories Sales Management System-<>-<>-<>")
    cursor = con.cursor()
    #creating table customers
    cursor.execute("CREATE TABLE customer(c_id INT PRIMARY KEY AUTO_INCREMENT,Name VARCHAR(40),Contact VARCHAR(15),Address VARCHAR(255)) AUTO_INCREMENT = 10001")
    print("Table CUSTOMER created succesfully.")
    #creating table products
    cursor.execute("CREATE TABLE products (P_ID INT PRIMARY KEY, Category VARCHAR(100), Name VARCHAR(500), Specifications VARCHAR(1000), Stock INT, Price FLOAT)")
    print("Table PRODUCTS created succesfully.")
    def insert_customer(): #insert details of customer
        while True:
            c_id=int(input("\nEnter Customer ID: "))
            name=input("\nEnter customer's name : ")
            contact=input("\nEnter customer's contact number : ")
            address=input("\nEnter your address : ")
            cursor.execute("INSERT into CUSTOMER(c_id, Name, Contact, Address) values(%s, %s, %s, %s)",(c_id, name, contact, address))
            con.commit()
            print("Details inserted successfully!")
            ch=input("Do you want to enter more records? (y/n)")
            if ch in 'Nn':
                break
    def update_customer(new_value, id_value): #update customer details
        up=int(input("What do you want to update? Enter 1 for updating customer's name, 2 for contact number, 3 for address : "))
        if up == 1:
            query = "UPDATE CUSTOMER SET Name = %s WHERE C_ID = %s;"
        elif up == 2:
            query = "UPDATE CUSTOMER SET Contact = %s WHERE C_ID = %s;"
        elif up == 3:
            query = "UPDATE CUSTOMER SET Address = %s WHERE C_ID = %s;"
        cursor.execute(query, (new_value, id_value))
        con.commit()
        print("Details updated successfully!")
    def insprod(pid,cname,specs,cstock,cprice):
        if(pid is None or cname is None or specs is None or cstock is None or cprice is None):
            print("All are required fields, can't be empty")
        else:
            cursor.execute("INSERT INTO products(P_ID, Name, Specifications, Stock, Price) VALUES (%s, %s, %s, %s, %s)",
             (pid, cname, specs, cstock, cprice))
            con.commit()
            print("Data inputted successfully!")
    def delprod(pid):
        if(pid is None):
            print("Required field, can't be empty")
        else:
            cursor.execute("delete from products where P_ID = %s",(pid,))
            con.commit()
            if cursor.rowcount > 0:
                print(f"Product with pid {pid} deleted successfully.")
            else:
                print(f"No product found with pid {pid}.")
    def delete_customer(id_value): #delete customer record
        query="DELETE FROM CUSTOMER where C_ID= %s"
        cursor.execute(query, (id_value,))
        con.commit()
        print("record deleted successfully")

    def view_customer():
        query="select * from  CUSTOMER"
        cursor.execute(query)
        results=cursor.fetchall()
        print("\n-------------------------------CUSTOMER-------------------------------")
        print(f"{'C_ID':<10} {'Name':<40} {'Specifications':<80} {'Stock':<10} {'Price':<10}")
        print() 
        for row in results:
            print(f"{row[0]:<10} {row[1]:<40} {row[2]:<80} {row[3]:<10}")

    i=1
    while i!=11:
        print("\n\n1. Insert Data into table Customer.\n2. Delete Data from table Customer.")
        print("3. Update Data of table Customer.\n4. View Data of table Customer.")
        print("\n5. Insert Data into table products\n6. Delete Data from table products.")
        print("7. Update Data of table products.\n8. View Data of table products.")
        print("\n9. Make Sales.\n10. View Sales.\n\n11. Exit")
        i=int(input("Enter choice (1/2/3/4/5/6/7/8/9/10/11): "))
        if i==1:
            insert_customer()
        elif i==2:
            id_value2=int(input("Enter customer id of customer whose detalis are to be deleted : "))
            delete_customer(id_value2)
        elif i==3:
            id_value1=int(input("Enter customer id of customer whose detalis are to be updated : "))
            new_value=input("Enter the value to be updated : ")
            update_customer(new_value,id_value1)
        elif i==4:
            view_customer()
        elif i==5:
            p_id=int(input("\n\nEnter Product ID: "))
            pname=input("\nEnter Name of the Product: ")
            specs=input("\nEnter Specifications of the above product (separated by commas): ")
            stock=int(input("\nHow many Stocks of the above product are left?: "))
            price=int(input("\nEnter the Price of the above product: ₹ "))
            if pname is None or specs is None or stock < 0 or price < 0:
                print("Required Fields, can't be empty.")
            else:
                insprod(p_id,pname,specs,stock,price)
        elif i==6:
            p_id=int(input("\n\nEnter product ID: "))
            delprod(p_id)
        elif i==7:
            p_id=int(input("\n\nEnter product ID: "))
            print("Update\n1. Name of the Product\n2. Specifications of Product\n3. Stock of Product\n4. Price of Product")
            c=int(input("Enter choice (1/2/3/4): "))
            if c==1:
                n=input("\nEnter new Name of the product: ")
                cursor.execute("UPDATE products SET Name = %s WHERE p_id = %s", (n, p_id))
                con.commit()
                print("Name updated successfully!")
            elif c==2:
                s=input("\nEnter new Specifications of the product: ")
                cursor.execute("UPDATE products SET Specifications = %s WHERE p_id = %s", (s, p_id))
                con.commit()
                print("Specifications Updated successfully!")
            elif c==3:
                st=input("\nEnter new Stock number of the product: ")
                cursor.execute("UPDATE products SET Stock = %s WHERE p_id = %s", (st, p_id))
                con.commit()
                print("Stock Number Updated successfully!")
            elif c==4:
                p=input("\nEnter new Specifications of the product: ")
                cursor.execute("UPDATE products SET Price = %s WHERE p_id = %s", (p, p_id))
                con.commit()
                print("Price Updated successfully!")
        elif i==8:
            print("\n-------------------------------PRODUCTS-------------------------------")
            cursor.execute("select * from products")
            results = cursor.fetchall()
            print(f"{'P_ID':<10} {'Name':<40} {'Contact':<80} {'Stock':<10} {'Address':<10}")
            print() 
            for row in results:
                print(f"{row[0]:<10} {row[1]:<40} {row[2]:<80} {row[3]:<10} {row[4]:<10}")
        elif i==11:
            cursor.close()
            con.close()
            print("Exitted successfully.")
        input("\nPress Enter to proceed...")
else:
    print("CONNECTION UNSUCCESSFUL!")