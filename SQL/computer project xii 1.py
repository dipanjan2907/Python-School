import mysql.connector as sqltor
# Establish connection to the database
con = sqltor.connect(
    host="localhost",
    user="group",
    password="G#n6Hg59",
    database="Computer_Sales_System")

if con.is_connected():
    print("||-------->>Connection successfully established<<--------||\n")
    print("<>-<>-<>-Welcome to Computer and Accessories Sales Management System-<>-<>-<>")
    cursor = con.cursor()
    # Creating table customers
    # cursor.execute("CREATE TABLE customer(Name VARCHAR(30), Contact VARCHAR(15) PRIMARY KEY, Address VARCHAR(255)) AUTO_INCREMENT = 10001")
    # print("Table CUSTOMER created successfully.")
    # Creating table products
    # cursor.execute("CREATE TABLE products (p_id INT PRIMARY KEY AUTO_INCREMENT, Category VARCHAR(100), Name VARCHAR(500), Specifications VARCHAR(1000), Stock INT, Price FLOAT) AUTO_INCREMENT = 51029")
    # print("Table PRODUCTS created successfully.")
    # Creating table Sales
    # cursor.execute("CREATE TABLE Sales (Customer_Name VARCHAR(30),Contact VARCHAR(15), Product_ID INT, Product_Name VARCHAR(500), Price_of_one FLOAT, Quantity INT, Total_Amount FLOAT)")
    # print("Table SALES created succesfully.")

    def insert_customer():  # Insert details of customer
        while True:
            name = input("\nEnter customer's name: ").title()
            contact = input("\nEnter customer's contact number: ")
            address = input("\nEnter customer's address: ")
            cursor.execute("INSERT INTO CUSTOMER (Name, Contact, Address) VALUES (%s, %s, %s)",
                           (name, contact, address))
            con.commit()
            print("Details inserted successfully!")
            ch = input("Do you want to enter more records? (y/n): ")
            if ch in 'Nn':
                break

    def update_customer(new_value, cont):  # Update customer details
        up = int(input("What do you want to update?\nEnter\n1 for updating customer's name\n2 for contact number\n3 for address\nchoice: "))
        if up == 1:
            query = "UPDATE CUSTOMER SET Name = %s WHERE Contact = %s;"
        elif up == 2:
            query = "UPDATE CUSTOMER SET Contact = %s WHERE Contact = %s;"
        elif up == 3:
            query = "UPDATE CUSTOMER SET Address = %s WHERE Contact = %s;"
        else:
            print("Invalid option!")
            return
        cursor.execute(query, (new_value, cont))
        con.commit()
        print("Details updated successfully!")

    def insprod():  # Insert data to table product
        while True: 
                cat=input("\nEnter Product Category: ").title()
                pname = input("\nEnter Name of the Product: ")
                specs = input("\nEnter Specifications of the above product (separated by commas): ").title()
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

    def delete_customer(cont):  # Delete customer record
        query = "DELETE FROM CUSTOMER WHERE CONTACT = %s"
        cursor.execute(query, (cont,))
        con.commit()
        print("Record deleted successfully.")

    def view_customer():  # Display table customer
        query = "SELECT * FROM CUSTOMER"
        cursor.execute(query)
        results = cursor.fetchall()
        print("-------------------------------CUSTOMER-------------------------------")
        print(f"{'Name':<40} {'Contact':<15} {'Address':<40}")
        print()
        for row in results:
            print(f"{row[0]:<40} {row[1]:<15} {row[2]:<40}")
    
    def search_by_product_name():
        n = input("Enter name of the Product to be searched: ")
        cursor.execute("SELECT Name FROM PRODUCTS WHERE Name = %s", (n,))
        result = cursor.fetchone()
        if result is not None:
            print("Found!\n")
            cursor.execute("SELECT * FROM PRODUCTS WHERE Name = %s", (n,))
            results = cursor.fetchall()
            if results:  # Check if results is not empty
                print(f"\n-------------------------------",n,"-------------------------------")
                print(f"{'P_ID':<10} {'Category':<30} {'Name':<25} {'Specifications':<70} {'Stock':<7} {'Price (₹)':<10}")
                print()
                for row in results:
                    print(f"{row[0]:<10} {row[1]:<30} {row[2]:<25} {row[3]:<70} {row[4]:<70} {row[5]:<10}")
                    return True
        else:
            print("\nSorry, NOT Found..")
            return False
    def check_customer_exists(cont):
        try:
            query = "SELECT 1 FROM Customer WHERE Contact = %s"
            cursor.execute(query, (cont,))
            result=cursor.fetchone()
            if result is None:
                ch=input("New Customer..Want to add to database? (Y/N)")
                if ch.lower()=='y':
                    insert_customer()
                else:
                    return 2
            else:
                print("Welcome Back!")
                return 1
        except sqltor.Error as e:
            print(f"Database error: {e}")
            return False
    def view_products():  # Display table products
        cursor.execute("SELECT * FROM PRODUCTS")
        results = cursor.fetchall()
        print("-------------------------------PRODUCTS-------------------------------")
        print(f"{'P_ID':<10} {'Category':<20} {'Name':<30} {'Specifications':<65} {'Stock':<10} {'Price (₹)':<10}")
        print()
        for row in results:
            print(f"{row[0]:<10} {row[1]:<20} {row[2]:<30} {row[3]:<65} {row[4]:<10} {row[5]:<10}")
    def category_view():
        cp = input("Enter Category (Laptop/Desktop/Processor, etc.): ").title()
        cursor.execute("SELECT * FROM PRODUCTS WHERE Category = %s", (cp,))
        results = cursor.fetchall()  # Fetch all results
        if results:  # Check if results is not empty
            print(f"\n------------------------------- {cp}s -------------------------------")
            print(f"{'P_ID':<10} {'Category':<30} {'Name':<25} {'Specifications':<70} {'Stock':<7} {'Price (₹)':<10}")
            print()
            for row in results:
                print(f"{row[0]:<10} {row[1]:<30} {row[2]:<25} {row[3]:<70} {row[4]:<7} {row[5]:<10}")
                return True
        else:
            print(f"\nNo products found in the '{cp}' category.")
            return False

        
    def check_product_stock(p_id, quantity):
        try:
            query = "SELECT stock FROM products WHERE p_id = %s"
            cursor.execute(query, (p_id,))
            result = cursor.fetchone()
            if result is not None:
                available_stock = result[0]
                if available_stock >= quantity:
                 return True
                else:
                    print("Insufficient stock!")
                    return False
            else:
                print("Product not found!")
                return False
        except sqltor.Error as e:
            print(f"Database error: {e}")
            return False
    def view_sales(): # Display table SALES
        query = "SELECT * FROM SALES"
        cursor.execute(query)
        results = cursor.fetchall()
        print("-------------------------------SALES-------------------------------")
        print(f"{'Customer_NAME':<30} {'Contact':<15} {'Product_ID':<10} {'Product_Name':<40} {'Price_of_1':<10} {'Quantity':<15} {'Total_Amount(₹)':<10}")
        print()
        for row in results:
            print(f"{row[0]:<30} {row[1]:<15} {row[2]:<10} {row[3]:<40} {row[4]:<10} {row[5]:<15} {row[6]:<10}")
    
    i = 1
    while i != 15:
        print("\n1. Insert Data into table Customer.\n2. Delete Data from table Customer.")
        print("3. Update Data of table Customer.\n4. View Data of table Customer.\n5. Check if New Customer.")
        print("\n6. Insert Data into table Products\n7. Delete Data from table Products.")
        print("8. Update Data of table Products.\n9. View Data of table Products.\n10. View Products by Category.")
        print("11. Check if Product Exists.\n\n12. Make Sale.\n13. View All Sales.\n14. View Purchase of a Particular Customer\n\n15. Exit")
        i = int(input("Enter choice (1/2/3/4/5/6/7/8/9/10/11/12): "))
        if i == 1:
            insert_customer()
        elif i == 2:
            c = int(input("Enter Contact of customer whose details are to be deleted: "))
            delete_customer(c)
        elif i == 3:
            c = int(input("Enter Contact of customer whose details are to be updated: "))
            new_value = input("Enter the value to be updated: ").title()
            update_customer(new_value, c)
        elif i == 4:
            view_customer()
        elif i==5:
            c=int(input("Enter Customer Phone Number:"))
            if check_customer_exists(c)==1:
                cursor.execute("SELECT * FROM CUSTOMER WHERE Contact=%s",(c,))
                results = cursor.fetchall()
                print(f"{'C_ID':<10} {'Name':<40} {'Contact':<15} {'Address':<40}")
                print()
                for row in results:
                    print(f"{row[0]:<10} {row[1]:<40} {row[2]:<15} {row[3]:<40}")
        elif i == 6:
            insprod()
        elif i == 7:
            p_id = int(input("\n\nEnter Product ID: "))
            delprod(p_id)
        elif i == 8:
            p_id = int(input("\n\nEnter Product ID: "))
            print("Update\n1. Name of the Product\n2. Specifications of Product\n3. Stock of Product\n4. Price of Product")
            c1 = int(input("Enter choice (1/2/3/4): "))
            if c1 == 1:
                n = input("\nEnter new Name of the product: ").title()
                cursor.execute("UPDATE PRODUCTS SET Name = %s WHERE P_ID = %s", (n, p_id))
                con.commit()
                print("Name updated successfully!")
            elif c1 == 2:
                s = input("\nEnter new Specifications of the product: ")
                cursor.execute("UPDATE PRODUCTS SET Specifications = %s WHERE P_ID = %s", (s, p_id))
                con.commit()
                print("Specifications updated successfully!")
            elif c1 == 3:
                st = int(input("\nEnter new Stock number of the product: "))
                cursor.execute("SELECT Stock FROM PRODUCTS WHERE p_id = %s", (p_id,))
                r=cursor.fetchone()
                st+=r[0]
                cursor.execute("UPDATE PRODUCTS SET Stock = %s WHERE P_ID = %s", (st, p_id))
                con.commit()
                print("Stock Number updated successfully!")
            elif c1 == 4:
                p = float(input("\nEnter new Price of the product: ₹ "))
                cursor.execute("UPDATE PRODUCTS SET Price = %s WHERE P_ID = %s", (p, p_id))
                con.commit()
                print("Price updated successfully!")
        elif i == 9:
            view_products()
        elif i == 10:
            category_view()
        elif i == 11:
            p = input("Enter Product Name: ").title()
            cursor.execute("SELECT Name FROM PRODUCTS WHERE Name = %s", (p,))
            results = cursor.fetchone()
            if results:
                cursor.execute("SELECT * FROM PRODUCTS WHERE Name = %s", (p,))
                results = cursor.fetchall()
                print("Product found!")
                print(f"{'P_ID':<10} {'Category':<20} {'Name':<30} {'Specifications':<65} {'Stock':<10} {'Price (₹)':<10}")
                print()
                for row in results:
                    print(f"{row[0]:<10} {row[1]:<20} {row[2]:<30} {row[3]:<65} {row[4]:<10} {row[5]:<10}")
            else:
                ch=input("New Product.....Want to add to database? (Y/N)")
                if ch.lower()=='y':
                    insprod()
        elif i == 12:
            c=int(input("Enter Customer Phone Number: "))
            if check_customer_exists(c)!=2:
                c12=int(input("1. Search Product by Name\n2. View Products by Category\nChoice (1/2): "))
                chk=0
                if c12==1:
                    if search_by_product_name()==True:
                        chk=1
                elif c12==2:
                    if category_view()==True:
                        chk=1
                if chk==1:
                    pid1=int(input("Enter Product ID (from table above): "))
                    quan=int(input("Quantity: "))
                    if check_product_stock(pid1,quan)==True:
                        cursor.execute("SELECT name, contact FROM Customer WHERE Contact = %s", (c,))
                        cust = cursor.fetchone()
                        cursor.execute("SELECT p_id, name, price FROM Products WHERE p_id = %s", (pid1,))
                        prod = cursor.fetchone()
                        if cust and prod:
                            total_amt = quan * prod[2] 
                            cursor.execute(
                            "INSERT INTO Sales ( Customer_Name, Contact, Product_ID, Product_Name, Price_of_one, Quantity, Total_Amount) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                            (cust[0], cust[1], prod[0], prod[1], prod[2], quan, total_amt))
                            con.commit()
                            print("Data successfully inserted into the Sales table.")
                            cursor.execute("UPDATE Products SET Stock = Stock - %s WHERE p_id = %s", (quan, prod[0]))
                            con.commit() 
                            print(f"Stock for product ID {prod[0]} updated successfully.")
                        else:
                            print("Customer or Product not found.")
                    else:
                        print("Not enough stock for the requested quantity.")
                else:
                        print("Product Not Found!")
        elif i == 13:
            view_sales()
        elif i==14:
            c=int(input("Enter Customer Phone Number: "))
            cursor.execute("SELECT * FROM SALES WHERE Contact= %s",(c,))
            results = cursor.fetchall()
            if results:
                print("--------------------------- PURCHASE BY ", results[0][0], "---------------------------")
                print(f"{'Customer_NAME':<30} {'Contact':<15} {'Product_ID':<10} {'Product_Name':<40} {'Price_of_1':<10} {'Quantity':<15} {'Total_Amount(₹)':<10}")
                print()
                for row in results:
                    print(f"{row[0]:<30} {row[1]:<15} {row[2]:<10} {row[3]:<40} {row[4]:<10} {row[5]:<15} {row[6]:<10}")
            else:
                print("No purchases found for the entered phone number.")
        elif i == 15:
            cursor.close()
            con.close()
            print("Exited successfully.\nTHANK YOU")
        input("\nPress Enter to proceed...")
else:
    print("CONNECTION UNSUCCESSFUL!")