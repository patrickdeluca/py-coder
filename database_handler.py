```python
import sqlite3
from models import Codebase

class DatabaseHandler:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS codebase (
                id INTEGER PRIMARY KEY,
                filename TEXT,
                code TEXT
            )
        """)
        self.conn.commit()

    def insert_code(self, codebase):
        self.cursor.execute("""
            INSERT INTO codebase (filename, code)
            VALUES (?, ?)
        """, (codebase.filename, codebase.code))
        self.conn.commit()

    def get_code(self, filename):
        self.cursor.execute("""
            SELECT code FROM codebase
            WHERE filename = ?
        """, (filename,))
        return self.cursor.fetchone()

    def update_code(self, codebase):
        self.cursor.execute("""
            UPDATE codebase
            SET code = ?
            WHERE filename = ?
        """, (codebase.code, codebase.filename))
        self.conn.commit()

    def delete_code(self, filename):
        self.cursor.execute("""
            DELETE FROM codebase
            WHERE filename = ?
        """, (filename,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()
```