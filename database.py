import sqlite3
import os
from app.core.config import settings

DB_FILE = "./marlin_x.db"

def init_db():
    """Initializes local SQLite database for fallback persistence."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS incidents (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        lat REAL NOT NULL,
        lon REAL NOT NULL,
        detected_at TEXT NOT NULL,
        oil_probability REAL NOT NULL,
        status TEXT NOT NULL,
        data_json TEXT
    );
    """)
    conn.commit()
    conn.close()

def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn
