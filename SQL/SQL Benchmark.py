import mysql.connector
import time

# MySQL Connection
conn = mysql.connector.connect(
   host="localhost",
    user="group",
    password="G#n6Hg59",
    database="Computer_Sales_System")
cursor = conn.cursor()

# Creating a test table (Run once)
cursor.execute("CREATE TABLE IF NOT EXISTS customertest (CUSTNUMB INT PRIMARY KEY AUTO_INCREMENT,CUSTNAME VARCHAR(255),ADDRESS VARCHAR(255),BALANCE FLOAT,CREDLIM FLOAT, SLSRNUMB INT)")
conn.commit()

# Sample Data
data = [(f"Name{i}", f"Address{i}", 1000.50, 5000.00, 3) for i in range(10000)]

# Single Insert (Slowest)
def single_insert():
    start_time = time.time()
    for row in data:
        cursor.execute("INSERT INTO customertest (CUSTNAME, ADDRESS, BALANCE, CREDLIM, SLSRNUMB) VALUES (%s, %s, %s, %s, %s)", row)
    conn.commit()
    return time.time() - start_time

# Batch Insert (Moderate Speed)
def batch_insert():
    start_time = time.time()
    cursor.executemany("INSERT INTO customertest (CUSTNAME, ADDRESS, BALANCE, CREDLIM, SLSRNUMB) VALUES (%s, %s, %s, %s, %s)", data)
    conn.commit()
    return time.time() - start_time

# Bulk Insert using LOAD DATA INFILE (Fastest)
def bulk_insert():
    with open("data.csv", "w") as f:
        for row in data:
            f.write(",".join(map(str, row)) + "\n")

    start_time = time.time()
    cursor.execute("""
        LOAD DATA INFILE 'data.csv'
        INTO TABLE customertest
        FIELDS TERMINATED BY ','
        LINES TERMINATED BY '\n'
        (CUSTNAME, ADDRESS, BALANCE, CREDLIM, SLSRNUMB)
    """)
    conn.commit()
    return time.time() - start_time

# Running Tests
print(f"Single Insert Time: {single_insert():.4f} sec")
print(f"Batch Insert Time: {batch_insert():.4f} sec")
print(f"Bulk Insert Time: {bulk_insert():.4f} sec")

# Cleanup (Optional)
cursor.execute("DROP TABLE customertest")
conn.commit()

# Closing Connection
cursor.close()
conn.close()