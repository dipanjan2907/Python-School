import mysql.connector as sqltor
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

# Establish connection to the database
con = sqltor.connect(
    host="localhost",
    user="group",
    password="G#n6Hg59",
    database="Computer_Sales_System"
)

cursor = con.cursor()

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Computer and Accessories Sales Management System")
        self.geometry("800x600")
        self.configure(bg="#2E3A47")  # Background color

        # Create a frame for the title
        title_frame = tk.Frame(self, bg="#344953")
        title_frame.pack(pady=20, fill=tk.X)
        
        title_label = tk.Label(title_frame, text="Sales Management System", font=("Helvetica", 24, "bold"), bg="#344953", fg="#FFFFFF")
        title_label.pack(pady=10)

        # Create buttons for different operations with styling
        button_frame = tk.Frame(self, bg="#2E3A47")
        button_frame.pack(pady=20)

        # Create a list of buttons
        button_texts = [
            "Insert Customer",
            "Delete Customer",
            "Update Customer",
            "View Customers",
            "Insert Product",
            "Delete Product",
            "Update Product",
            "View Products",
            "Exit"
        ]
        
        for text in button_texts:
            btn = tk.Button(button_frame, text=text, command=self.get_command(text), font=("Helvetica", 14), bg="#4C6B79", fg="#FFFFFF", width=20)
            btn.pack(pady=10)

    def get_command(self, action):
        commands = {
            "Insert Customer": self.insert_customer,
            "Delete Customer": self.delete_customer,
            "Update Customer": self.update_customer,
            "View Customers": self.view_customers,
            "Insert Product": self.insert_product,
            "Delete Product": self.delete_product,
            "Update Product": self.update_product,
            "View Products": self.view_products,
            "Exit": self.exit_program
        }
        return commands.get(action)

    def insert_customer(self):
        name = simpledialog.askstring("Input", "Enter customer's name:")
        contact = simpledialog.askstring("Input", "Enter customer's contact number:")
        address = simpledialog.askstring("Input", "Enter customer's address:")
        
        if name and contact and address:
            cursor.execute("INSERT INTO CUSTOMER (Name, Contact, Address) VALUES (%s, %s, %s)", (name, contact, address))
            con.commit()
            messagebox.showinfo("Success", "Customer inserted successfully!")
        else:
            messagebox.showwarning("Input Error", "All fields are required!")

    def delete_customer(self):
        c_id = simpledialog.askinteger("Input", "Enter Customer ID to delete:")
        cursor.execute("DELETE FROM CUSTOMER WHERE C_ID = %s", (c_id,))
        con.commit()
        if cursor.rowcount > 0:
            messagebox.showinfo("Success", f"Customer with ID {c_id} deleted successfully.")
        else:
            messagebox.showwarning("Not Found", f"No customer found with ID {c_id}.")

    def update_customer(self):
        c_id = simpledialog.askinteger("Input", "Enter Customer ID to update:")
        name = simpledialog.askstring("Input", "Enter new name (leave blank to skip):")
        contact = simpledialog.askstring("Input", "Enter new contact (leave blank to skip):")
        address = simpledialog.askstring("Input", "Enter new address (leave blank to skip):")
        
        updates = []
        if name:
            updates.append(f"Name = '{name}'")
        if contact:
            updates.append(f"Contact = '{contact}'")
        if address:
            updates.append(f"Address = '{address}'")
        
        if updates:
            query = f"UPDATE CUSTOMER SET {', '.join(updates)} WHERE C_ID = %s"
            cursor.execute(query, (c_id,))
            con.commit()
            messagebox.showinfo("Success", "Customer updated successfully!")
        else:
            messagebox.showwarning("No Update", "No changes made.")

    def view_customers(self):
        cursor.execute("SELECT * FROM CUSTOMER")
        results = cursor.fetchall()
        view_window = tk.Toplevel(self)
        view_window.title("Customers")
        view_window.geometry("600x400")
        view_window.configure(bg="#F3F4F6")

        tk.Label(view_window, text="Customers List", font=("Helvetica", 18), bg="#F3F4F6").pack(pady=10)

        for row in results:
            tk.Label(view_window, text=f"{row[0]}: {row[1]}, {row[2]}, {row[3]}", bg="#F3F4F6").pack()

    def insert_product(self):
        name = simpledialog.askstring("Input", "Enter product name:")
        specs = simpledialog.askstring("Input", "Enter specifications:")
        stock = simpledialog.askinteger("Input", "Enter stock quantity:")
        price = simpledialog.askfloat("Input", "Enter price:")
        
        if name and specs and stock is not None and price is not None:
            cursor.execute("INSERT INTO PRODUCTS (Name, Specifications, Stock, Price) VALUES (%s, %s, %s, %s)",
                           (name, specs, stock, price))
            con.commit()
            messagebox.showinfo("Success", "Product inserted successfully!")
        else:
            messagebox.showwarning("Input Error", "All fields are required!")

    def delete_product(self):
        p_id = simpledialog.askinteger("Input", "Enter Product ID to delete:")
        cursor.execute("DELETE FROM PRODUCTS WHERE P_ID = %s", (p_id,))
        con.commit()
        if cursor.rowcount > 0:
            messagebox.showinfo("Success", f"Product with ID {p_id} deleted successfully.")
        else:
            messagebox.showwarning("Not Found", f"No product found with ID {p_id}.")

    def update_product(self):
        p_id = simpledialog.askinteger("Input", "Enter Product ID to update:")
        name = simpledialog.askstring("Input", "Enter new name (leave blank to skip):")
        specs = simpledialog.askstring("Input", "Enter new specifications (leave blank to skip):")
        stock = simpledialog.askinteger("Input", "Enter new stock (leave blank to skip):")
        price = simpledialog.askfloat("Input", "Enter new price (leave blank to skip):")
        
        updates = []
        if name:
            updates.append(f"Name = '{name}'")
        if specs:
            updates.append(f"Specifications = '{specs}'")
        if stock is not None:
            updates.append(f"Stock = {stock}")
        if price is not None:
            updates.append(f"Price = {price}")
        
        if updates:
            query = f"UPDATE PRODUCTS SET {', '.join(updates)} WHERE P_ID = %s"
            cursor.execute(query, (p_id,))
            con.commit()
            messagebox.showinfo("Success", "Product updated successfully!")
        else:
            messagebox.showwarning("No Update", "No changes made.")

    def view_products(self):
        cursor.execute("SELECT * FROM PRODUCTS")
        results = cursor.fetchall()
        view_window = tk.Toplevel(self)
        view_window.title("Products")
        view_window.geometry("600x400")
        view_window.configure(bg="#F3F4F6")

        tk.Label(view_window, text="Products List", font=("Helvetica", 18), bg="#F3F4F6").pack(pady=10)

        for row in results:
            tk.Label(view_window, text=f"{row[0]}: {row[1]}, {row[2]}, Stock: {row[3]}, Price: ₹{row[4]}", bg="#F3F4F6").pack()

    def exit_program(self):
        cursor.close()
        con.close()
        self.destroy()

if __name__ == "__main__":
    app = Application()
    app.mainloop()
