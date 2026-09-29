import os
import sys
import psycopg2
import mysql.connector





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


connection = connection_mysql.cursor()

connection.execute("SHOW FULL TABLES WHERE Table_type = 'BASE TABLE';")
tables = connection.fetchall()
for table in tables:
    print("Table name:", table)
    print(f"Content:" connection.execute(f'SELECT * FROM table'))
