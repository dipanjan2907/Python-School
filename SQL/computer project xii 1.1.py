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

    def check_customer_exists(cname):
        try:
            query = "SELECT 1 FROM Customer WHERE Name = %s"
            cursor.execute(query, (cname,))
            result = cursor.fetchone()
            if result is None:
                print("New Customer?..Adding to Database.")
                insert_customer()
            else:
                print("Welcome Back!")
        except sqltor.Error as e:
            print(f"Database error: {e}")
            return False

    def check_product_stock(p_id, quantity):
        try:
            query = "SELECT Stock FROM PRODUCTS WHERE P_ID = %s"
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

    def make_sale():
        cname = input("Enter Customer Name: ").title()
        check_customer_exists(cname)
        c12 = int(input("1. Search Product by Name\n2. View Products by Category\nChoice (1/2): "))
        chk = 0
        if c12 == 1:
            if search_by_product_name():
                chk = 1
        elif c12 == 2:
            if category_view():
                chk = 1

        if chk == 1:
            pid1 = int(input("Enter Product ID (from table above): "))
            quan = int(input("Quantity: "))
            if check_product_stock(pid1, quan):
                cursor.execute("SELECT c_id, name FROM Customer WHERE name = %s", (cname,))
                cust = cursor.fetchone()
                cursor.execute("SELECT p_id, name, price FROM Products WHERE p_id = %s", (pid1,))
                prod = cursor.fetchone()

                if cust and prod:
                    total_amt = quan * prod[2]
                    cursor.execute(
                        "INSERT INTO SALES (Customer_ID, Customer_Name, Product_ID, Product_Name, Price(1), Quantity, Total_Amount) "
                        "VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                        (cust[0], cust[1], prod[0], prod[1], prod[2], quan, total_amt)
                    )
                    con.commit()
                    print("Data successfully inserted into the Sales table.")
                    
                    # Update stock after sale
                    cursor.execute("UPDATE PRODUCTS SET Stock = Stock - %s WHERE P_ID = %s", (quan, prod[0]))
                    con.commit()
                else:
                    print("Customer or Product not found.")
            else:
                print("Purchase can't be made...retry with lesser quantity!")
        else:
            print("Product Not Found!")

    # Main loop
    i = 1
    while i != 12:
        print("\n1. Insert Data into table Customer.\n2. Delete Data from table Customer.")
        print("3. Update Data of table Customer.\n4. View Data of table Customer.")
        print("\n5. Insert Data into table Products\n6. Delete Data from table Products.")
        print("7. Update Data of table Products.\n8. View Data of table Products.\n9. View Products by Category.")
        print("\n10. Make Sale.\n11. View Sales.\n\n12. Exit")
        i = int(input("Enter choice (1/2/3/4/5/6/7/8/9/10/11/12): "))
        if i == 1:
            insert_customer()
        elif i == 2:
            id_value2 = int(input("Enter customer ID of customer whose details are to be deleted: "))
            delete_customer(id_value2)
        elif i == 3:
            id_value1 = int(input("Enter customer ID of customer whose details are to be updated: "))
            new_value = input("Enter the value to be updated: ").title()
            update_customer(new_value, id_value1)
        elif i == 4:
            view_customer()
        elif i == 5:
            insprod()
        elif i == 6:
            p_id = int(input("Enter the Product ID of the product to be deleted: "))
            delprod(p_id)
        elif i == 7:
            pid = int(input("Enter Product ID of product whose details are to be updated: "))
            update_product(pid)
        elif i == 8:
            view_products()
        elif i == 9:
            category_view()
        elif i == 10:
            make_sale()  # Calling make_sale function
        elif i == 11:
            view_sales()
        elif i == 12:
            print("Exiting...")
            break
else:
    print("Connection failed!")
