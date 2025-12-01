import sqlite3
import os
from src.core.config import settings

def get_connection():
    db_path = settings.DB_PATH
    #creating directory automatically if it doesn't exist
    folder = os.path.dirname(db_path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)

    #creating and return SQLite connection
    return sqlite3.connect(db_path)
