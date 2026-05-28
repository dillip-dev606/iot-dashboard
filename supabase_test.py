import psycopg2

conn = psycopg2.connect(
    host="db.udsqqzlijvkypxbbepxf.supabase.co",
    port="5432",
    database="postgres",
    user="postgres",
    password="Dillip@2004@"
)

print("Connected to Supabase!")

cursor = conn.cursor()

cursor.execute("SELECT version();")

version = cursor.fetchone()

print(version)

cursor.close()
conn.close()