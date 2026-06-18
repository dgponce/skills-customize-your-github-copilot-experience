import sqlite3
from pathlib import Path

DB = Path(__file__).parent / 'data.db'

def init_db():
    with sqlite3.connect(DB) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, title TEXT, body TEXT)')

def add_note(title, body):
    with sqlite3.connect(DB) as conn:
        conn.execute('INSERT INTO notes (title, body) VALUES (?, ?)', (title, body))

if __name__ == '__main__':
    init_db()
    add_note('Sample', 'This is a sample note')
    print('DB initialized and sample note added')
