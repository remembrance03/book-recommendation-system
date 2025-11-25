import sqlite3

#connecting and creating file if not exists
conn = sqlite3.connect("books.db")
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

print("Database and table created successfully!")
