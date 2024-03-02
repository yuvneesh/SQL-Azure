import os
import pyodbc
from dotenv import load_dotenv

load_dotenv()

# In flask, this conn is achieved via sqlite_connection
conn = pyodbc.connect(f"Driver={{ODBC Driver 18 for SQL Server}};Server=tcp:{os.getenv('HOST')},1433;Database=dbMain;Uid={os.getenv('USERNAME')};Pwd={os.getenv('PASSWORD')};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")

cursor = conn.cursor()
cursor.execute("SELECT * FROM LoginAppCreds")
results = cursor.fetchall()
print([result for result in results])
conn.close()