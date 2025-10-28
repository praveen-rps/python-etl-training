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

# step-3 : write a query and execute SQL query
query = "SELECT * FROM users"
csr.execute(query)


# step-4 : process the results
data = csr.fetchall()

for row in data:
    print(row)


# step-5 : close the cursor and connection

csr.close()
conn.close()