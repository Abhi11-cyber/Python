import oracledb

# Initialize Oracle Instant Client (thick mode)
oracledb.init_oracle_client(lib_dir=r"C:\Users\abhis\Downloads\oracle instant client\instantclient_23_7")

# 2. Connect to Oracle Database
connection = oracledb.connect(
    user="SYSTEM",
    password="ABHI11",
    dsn="127.0.0.1:1521/XE"
)

# 3. Use database
cursor = connection.cursor()
cursor.execute("SELECT * FROM student")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
connection.close()
