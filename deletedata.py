import mysql.connector

# step-1 : establish the connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="kyndryl"
)

# step-2 : create a cursor object
csr = conn.cursor()
query = "delete from users where id=%s"
id = int(input("Enter the ID: "))

data = (id,)
# step-3 : write a query to insert and execute SQL query
#query = "insert into users (id, name, age,email) values (5, 'Ali', 36,'Ali@gmail.com')"
#query = "insert into users (id, name, age,email) values (%s, %s, %s, %s)"
csr.execute(query,data)
conn.commit()
print(csr.rowcount , "records (s) deleted successfully.")

# step-5 : close the cursor and connection

csr.close()
conn.close()