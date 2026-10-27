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

# Map MySQL data types to PostgreSQL data types
type_mapping = {
    'int': 'INT',
    'tinyint': 'SMALLINT',
    'text' : 'TEXT',
    'date' : 'DATE',
    'datetime' : 'TIMESTAMP',
    'smallint' : 'SMALLINT',
    }

# Fetch tables and columns from MySQL database
with connection_mysql.cursor() as mysql_cursor, connection_pg.cursor() as pg_cursor:
    mysql_cursor.execute("SHOW TABLES;")
    tables = mysql_cursor.fetchall()

    # Iterate through each table and fetch its columns
    for table in tables:
        table_name = table[0]
        print(f"Creating table: {table_name}...")

        mysql_cursor.execute(f"DESCRIBE {table_name};")
        columns = mysql_cursor.fetchall()

        # Iterate through each column and print its name and type
        columns_sql = []
        pk_columns = []
        for column in columns:
            column_name = column[0]
            column_type = column[1]

            pg_type = type_mapping.get(column_type, column_type.upper())

            # Handle primary key and auto-increment columns
            if column[3] == 'PRI' and column[5] == 'auto_increment':
                col_def = f"{column_name} SERIAL"
            else:
                col_def = f"{column_name} {pg_type}"

            if column[3] == 'PRI':
                pk_columns.append(column_name)

            columns_sql.append(col_def)

        if pk_columns:
            pk_columns_str = ", ".join(pk_columns)
            columns_sql.append(f"PRIMARY KEY ({pk_columns_str})")

        columns_definition = ", ".join(columns_sql)
        create_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_definition});"

        pg_cursor.execute(create_query)

# Commit the changes to the PostgreSQL database
connection_pg.commit()
print("All tables successfully created in PostgreSQL database.")