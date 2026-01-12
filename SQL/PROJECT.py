import mysql.connector as sqltor
# Establish connection to the database
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
    # Creating table customers
    # cursor.execute("CREATE TABLE customer(c_id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(40), Contact VARCHAR(15), Address VARCHAR(255)) AUTO_INCREMENT = 10001")
    # print("Table CUSTOMER created successfully.")
    # Creating table products
    #cursor.execute("CREATE TABLE products (P_ID INT PRIMARY KEY AUTO_INCREMENT, Category VARCHAR(100), Name VARCHAR(500), Specifications VARCHAR(1000), Stock INT, Price FLOAT) AUTO_INCREMENT = 51029")
    # print("Table PRODUCTS created successfully.")

    def insert_customer():  # Insert details of customer
        while True:
            name = input("\nEnter customer's name: ")
            contact = input("\nEnter customer's contact number: ")
            address = input("\nEnter customer's address: ")
            cursor.execute("INSERT INTO CUSTOMER (Name, Contact, Address) VALUES (%s, %s, %s)",
                           (name, contact, address))
            con.commit()
            print("Details inserted successfully!")
            ch = input("Do you want to enter more records? (y/n): ")
            if ch in 'Nn':
                break

    def update_customer(new_value, id_value):  # Update customer details
        up = int(input("What do you want to update?\nEnter\n1 for updating customer's name\n2 for contact number\n3 for address\nchoice: "))
        if up == 1:
            query = "UPDATE CUSTOMER SET Name = %s WHERE C_ID = %s;"
        elif up == 2:
            query = "UPDATE CUSTOMER SET Contact = %s WHERE C_ID = %s;"
        elif up == 3:
            query = "UPDATE CUSTOMER SET Address = %s WHERE C_ID = %s;"
        else:
            print("Invalid option!")
            return
        cursor.execute(query, (new_value, id_value))
        con.commit()
        print("Details updated successfully!")

    def insprod():  # Insert data to table product
        while True: 
                cat=input("\nEnter Product Category: ")
                pname = input("\nEnter Name of the Product: ")
                specs = input("\nEnter Specifications of the above product (separated by commas): ")
                stock = int(input("\nHow many Stocks of the above product are left?: "))
                price = float(input("\nEnter the Price of the above product: ₹ "))
                cursor.execute("INSERT INTO PRODUCTS (Category, Name, Specifications, Stock, Price) VALUES (%s, %s, %s, %s, %s)",
                       (cat, pname, specs, stock, price))
                con.commit()
                print("Data inserted successfully!")
                ch = input("Do you want to enter more records? (y/n): ")
                if ch in 'Nn':
                    break

    def delprod(pid):  # Delete product record
        cursor.execute("DELETE FROM PRODUCTS WHERE P_ID = %s", (pid,))
        con.commit()
        if cursor.rowcount > 0:
            print(f"Product with P_ID {pid} deleted successfully.")
        else:
            print(f"No product found with P_ID {pid}.")

    def delete_customer(id_value):  # Delete customer record
        query = "DELETE FROM CUSTOMER WHERE C_ID = %s"
        cursor.execute(query, (id_value,))
        con.commit()
        print("Record deleted successfully.")

    def view_customer():  # Display table customer
        query = "SELECT * FROM CUSTOMER"
        cursor.execute(query)
        results = cursor.fetchall()
        print("-------------------------------CUSTOMER-------------------------------")
        print(f"{'C_ID':<10} {'Name':<40} {'Contact':<15} {'Address':<40}")
        print()
        for row in results:
            print(f"{row[0]:<10} {row[1]:<40} {row[2]:<15} {row[3]:<40}")

    def view_products():  # Display table products
        cursor.execute("SELECT * FROM PRODUCTS")
        results = cursor.fetchall()
        print("-------------------------------PRODUCTS-------------------------------")
        print(f"{'P_ID':<10} {'Name':<40} {'Specifications':<80} {'Stock':<10} {'Price':<10}")
        print()
        for row in results:
            print(f"{row[0]:<10} {row[1]:<40} {row[2]:<80} {row[3]:<10} {row[4]:<10}")

    i = 1
    while i != 12:
        print("\n1. Insert Data into table Customer.\n2. Delete Data from table Customer.")
        print("3. Update Data of table Customer.\n4. View Data of table Customer.")
        print("\n5. Insert Data into table Products\n6. Delete Data from table Products.")
        print("7. Update Data of table Products.\n8. View Data of table Products.\n9. View Products by Category.")
        print("\n10. Make Sales.\n11. View Sales.\n\n12. Exit")
        i = int(input("Enter choice (1/2/3/4/5/6/7/8/9/10/11/12): "))
        if i == 1:
            insert_customer()
        elif i == 2:
            id_value2 = int(input("Enter customer ID of customer whose details are to be deleted: "))
            delete_customer(id_value2)
        elif i == 3:
            id_value1 = int(input("Enter customer ID of customer whose details are to be updated: "))
            new_value = input("Enter the value to be updated: ")
            update_customer(new_value, id_value1)
        elif i == 4:
            view_customer()
        elif i == 5:
            insprod()
        elif i == 6:
            p_id = int(input("\n\nEnter Product ID: "))
            delprod(p_id)
        elif i == 7:
            p_id = int(input("\n\nEnter Product ID: "))
            print("Update\n1. Name of the Product\n2. Specifications of Product\n3. Stock of Product\n4. Price of Product")
            c = int(input("Enter choice (1/2/3/4): "))
            if c == 1:
                n = input("\nEnter new Name of the product: ")
                cursor.execute("UPDATE PRODUCTS SET Name = %s WHERE P_ID = %s", (n, p_id))
                con.commit()
                print("Name updated successfully!")
            elif c == 2:
                s = input("\nEnter new Specifications of the product: ")
                cursor.execute("UPDATE PRODUCTS SET Specifications = %s WHERE P_ID = %s", (s, p_id))
                con.commit()
                print("Specifications updated successfully!")
            elif c == 3:
                st = int(input("\nEnter new Stock number of the product: "))
                cursor.execute("UPDATE PRODUCTS SET Stock = %s WHERE P_ID = %s", (st, p_id))
                con.commit()
                print("Stock Number updated successfully!")
            elif c == 4:
                p = float(input("\nEnter new Price of the product: "))
                cursor.execute("UPDATE PRODUCTS SET Price = %s WHERE P_ID = %s", (p, p_id))
                con.commit()
                print("Price updated successfully!")
        elif i == 8:
            view_products()
        elif i == 9:
            c=input("Enter Category (Laptop/Desktop/Processor, etc..): ")
            cursor.execute("SELECT * FROM PRODUCTS WHERE Category = %s",(c,))
            results = cursor.fetchall()
            print("-------------------------------",c,"s-------------------------------")
            print(f"{'P_ID':<10} {'Category':<30} {'Name':<25} {'Specifications':<70} {'Stock':<7} {'Price (₹)':<10}")
            print()
            for row in results:
                print(f"{row[0]:<10} {row[1]:<30} {row[2]:<25} {row[3]:<70} {row[4]:<7} {row[5]:<10}")
        elif i == 10:
            print("UNDER DEVELOPMENT")
        elif i == 11:
            print("UNDER DEVELOPMENT")
        elif i == 12:
            cursor.close()
            con.close()
            print("Exited successfully.\nTHANK YOU")
        input("\nPress Enter to proceed...")
else:
    print("CONNECTION UNSUCCESSFUL!")