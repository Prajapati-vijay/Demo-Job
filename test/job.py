import pyodbc
import os
# Configuration
server = os.getenv("DBHOST")         # e.g., 'localhost' or '192.168.1.10'
database = 'VEDW'     # e.g., 'MyDB'
username = os.getlogin("USER")
password = os.getenv("PASS")
driver = '{ODBC Driver 17 for SQL Server}'  # Ensure this is installed

# Connect to SQL Server
try:
    conn = pyodbc.connect(
        f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    )
    cursor = conn.cursor()
    print("✅ Connected to the database successfully.")
except Exception as e:
    print("❌ Failed to connect to the database:", e)
    exit()

# Define your SQL query
query = "select * from Portfolio.holding where VESecID=326460 and HoldingDate='2019-11-13'"  # Adjust the table/schema/case

# Execute the query
try:
    cursor.execute(query)
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()

    print("✅ Query Results:")
    print(columns)
    for row in rows:
        print(row)

except Exception as e:
    print("❌ Query failed:", e)

# Close the connection
cursor.close()
conn.close()
