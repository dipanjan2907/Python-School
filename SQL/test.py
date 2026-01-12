import mysql.connector as sqltor # type: ignore
connection = sqltor.connect(
    host="localhost",
    user="root",
    password="Password@MySQL1",
    database="Office"
)
if connection.is_connected():
    print("||-------->>Connection successfully established<<--------||")
    cursor = connection.cursor()
    #for input
    cursor.execute("insert into purchase(Serial,Name,Price,Number) values({},'{}',{},{})".format(4,'Galaxy Book 4 Pro',153000,1))
    connection.commit()
    #cursor.execute("select * from employee")
    cursor.execute("select * from employee where location in ('Bally')")
    results = cursor.fetchall()
    if not results:
        print("No results found.")
    else:
        for row in results:
            print(row)
    cursor.close()
    connection.close()
else:
    print("Failed to establish connection.")