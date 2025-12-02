import sqlite3
import csv
from src.core.db_connection import get_connection

def insert_books_from_csv(csv_file_path: str):
    #reading CSV
    with open(csv_file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        books = [(row['title'], row['genre'], row['author'], row['summary']) for row in reader]

    #inserting into DB
    conn = get_connection()
    cursor = conn.cursor()

    #inserting books
    cursor.executemany(
        "INSERT INTO books (title, genre, author, summary) VALUES (?, ?, ?, ?)",
        books
    )
    conn.commit()
    conn.close()  