import sqlite3
import pandas as pd


#Method to create a sqlite table with fileds id, name, age, email
def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS students
                          (htno INTEGER PRIMARY KEY, name TEXT, total INTEGER, result TEXT)''')
        conn.commit()
        print("Table created successfully")
    except sqlite3.Error as e:
        print("Error creating table:", e)



# Method to create sqlite connection
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn


# Method to read the data from a csv file and return the dataframe
def read_csv_data(file_path):
    df = pd.read_csv(file_path)
    return df

# Method to insert data from dataframe to sqlite table
def insert_data_to_db(conn, df, table_name):
    try:
        df.to_sql(table_name, conn, if_exists='append', index=False)
        print("Data inserted successfully into the table:", table_name)
    except Exception as e:
        print("Error inserting data into table:", e)

def clean_data(df):
   df['total'].fillna(0, inplace=True)
   df.dropna(subset=['htno', 'name'], inplace=True)
   df['total'] = pd.to_numeric(df['total'], errors='coerce').fillna(0).astype(int)
   return df 

def calculate_result(df):
   def get_result(total):
       if total >=80:
              return 'Distinction'
       elif total >=70 and total< 80:
              return 'First Class'
       elif total >=60 and total< 70:
              return 'Second Class'
       elif total >=50 and total< 60:
              return 'Third Class'
       else:
              return 'Fail'
   df['result'] = df['total'].apply(get_result)   
   return df

if __name__ == '__main__':
    database = 'kyndryl.db'
    csv_file_path = 'rawdata.csv'
    table_name = 'students'

    # Create a database connection
    conn = create_connection(database)
    create_table(conn)
    # Read data from CSV file
    df = read_csv_data(csv_file_path)
    cleaneddata = clean_data(df)
    print(df)
    calculateddata = calculate_result(cleaneddata)
    print(df)
    insert_data_to_db(conn, calculateddata, table_name)
    print("Results are calculated from csv file and successfully inserted into the database.")