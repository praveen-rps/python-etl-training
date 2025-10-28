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

id = int(input("Enter the ID: "))
name = input("Enter the Name: ")
age = int(input("Enter the Age: "))
email = input("Enter the Email: ")
data = (id, name, age, email)
# step-3 : write a query to insert and execute SQL query
#query = "insert into users (id, name, age,email) values (5, 'Ali', 36,'Ali@gmail.com')"
query = "insert into users (id, name, age,email) values (%s, %s, %s, %s)"
csr.execute(query,data)
conn.commit()
print("Data Inserted..!")

# step-5 : close the cursor and connection

csr.close()
conn.close()