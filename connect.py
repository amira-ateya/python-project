import psycopg2

conn = psycopg2.connect(
    dbname="loan_project",
    user="iti",
    password="amira12345",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()
cursor.execute("SELECT version();")
print("Connected to:", cursor.fetchone())

cursor.close()
conn.close()
