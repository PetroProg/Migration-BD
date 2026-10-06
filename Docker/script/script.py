import os
import sys
import psycopg2
import mysql.connector

# Extract PostgreSQL database connection parameters from environment variables
try:
    connection_pg = psycopg2.connect(database=os.getenv('POSTGRES_DB'), 
                                    user=os.getenv('POSTGRES_USER'), 
                                    password=os.getenv('POSTGRES_PASSWORD'), 
                                    host=os.getenv('POSTGRES_HOST'), 
                                    port=os.getenv('POSTGRES_PORT'))
except psycopg2.Error as e:
    print(f"Error connecting to PostgreSQL database: {e}")
    connection_pg = None
    sys.exit(1)
else:
    print("Connected to PostgreSQL database successfully.")

# Extract MySQL connection parameters from environment variables
try:
    connection_mysql = mysql.connector.connect(user=os.getenv('MYSQL_USER'), 
                                                password=os.getenv('MYSQL_PASSWORD'), 
                                                host=os.getenv('MYSQL_HOST'), 
                                                database=os.getenv('MYSQL_DATABASE'))
except mysql.connector.Error as e:
    print(f"Error connecting to MySQL database: {e}")
    connection_mysql = None
    sys.exit(1)
else:
    print("Connected to MySQL database successfully.")

# Fetch tables and columns from MySQL database
with connection_mysql.cursor() as cursor:
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    # Iterate through each table and fetch its columns
    for table in tables:
        table_name = table[0]
        print("Table name:", table_name)
        cursor.execute(f"DESCRIBE {table_name};")
        columns = cursor.fetchall()
        # Iterate through each column and print its name and type
        for column in columns:
            column_name = column[0]
            column_type = column[1]
            print(f"Column name: {column_name}, Column type: {column_type}")
            if column_type.startswith("PRIMARY KEY"):
                print(f"Column {column_name} is a primary key.")
            elif column_type.startswith("FOREIGN KEY"):
                print(f"Column {column_name} is a foreign key.")

# Map MySQL data types to PostgreSQL data types
type_mapping = {
    'int': 'INT',
    'tinyint': 'SMALLINT',
    'text' : 'TEXT',
    'date' : 'DATE',
    'datetime' : 'TIMESTAMP',
    'smallint' : 'SMALLINT',
    }

# Generate PostgreSQL column definition based on MySQL column attributes
pg_type = type_mapping.get(column_type, column_type.upper())

# Generate PostgreSQL column definition based on MySQL column attributes
if column[3] == 'PRI' and column[5] == 'auto_increment':
    x = f"{column_name} SERIAL PRIMARY KEY"
elif column[3] == 'PRI':
    x = f"{column_name} {pg_type} PRIMARY KEY"
else:
    x = f"{column_name} {pg_type}"

