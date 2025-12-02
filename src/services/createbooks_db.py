from src.core.db_connection import get_connection

#connecting and creating file if not exists
conn = get_connection()
cursor = conn.cursor()

#creating table
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    genre TEXT,
    author TEXT,
    summary TEXT
)
""")

conn.commit()
conn.close()

print("Table created successfully!")
