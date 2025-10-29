import mysql.connector
import sqlite3
# step-1 : establish the connection

"""
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="kyndryl"
)
"""
conn = sqlite3.connect('kyndryl.db')

# step-2 : create a cursor object
csr = conn.cursor()
query = "update users set name=?, age=?, email=? where id=?"
id = int(input("Enter the ID: "))
name = input("Enter the new Name: ")
age = int(input("Enter the new Age: "))
email = input("Enter the new Email: ")
data = (name, age, email,id)
# step-3 : write a query to insert and execute SQL query
#query = "insert into users (id, name, age,email) values (5, 'Ali', 36,'Ali@gmail.com')"
#query = "insert into users (id, name, age,email) values (%s, %s, %s, %s)"
csr.execute(query,data)
conn.commit()
print(csr.rowcount , "record (s) updated successfully.")

# step-5 : close the cursor and connection

csr.close()
conn.close()